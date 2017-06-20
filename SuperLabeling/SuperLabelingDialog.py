##################################################################################
#
#               Dialog and main body of this plugin
#
##################################################################################
from PyQt4.QtGui import (QDialog, QDialogButtonBox, QProgressBar, QMessageBox)
from PyQt4 import QtGui, QtCore
from qgis.core import QgsMapLayer, QgsField
import share

from ui import Ui_Dialog
from getCoordinate import getCoordinate


class SuperLabelingDialog(QDialog, Ui_Dialog):
    
    def __init__(self, iface):
        # initialize EasyMinimumLabelingDialog class
        super(self.__class__, self).__init__(None, QtCore.Qt.WindowStaysOnTopHint) 
        #QtGui.QDialog.__init__(self, None, Qt.WindowStaysOnTopHint) # another method to initialize
        self.iface = iface
        
        # Set up the user interface from Designer.
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        # prepare map tool for using defined QgsMapToolIdentify
        self.mapTool = getCoordinate(self.iface)
        
        # connect signal to function and set variable
        #self.ui.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.write)
        self.ui.buttonBox.button(QDialogButtonBox.Apply).clicked.connect(self.write)
        self.ui.txX.setText("")#"No, I cant!")
        self.ui.txY.setText("")#"Yes, you can!")
        self.ui.txLayer.setText("")
        self.ui.cbField.clear()
        global flag_create, field_list, flag_vectorLayer, flag_init
        flag_create = False
        flag_vectorLayer = False
        field_list = []
        flag_init = False
        
        # check layer
        self.checkLayer()
        # when curren layer changed, check the layer
        self.iface.currentLayerChanged.connect(self.checkLayer)
        
        
    def checkLayer(self):
        global flag_vectorLayer
        # get current layer
        layer = self.iface.mapCanvas().currentLayer()
        
        # decide the layer type and show some message to dialog
        if (layer) and layer.type() == QgsMapLayer.VectorLayer:
            flag_vectorLayer = True
            self.trueSet()
            self.ui.cbField.clear()
            infoString = unicode('1. Choose the field you want to Label, click "Generate" for label fields')
            self.ui.lbStep1.setText(infoString)
            # set current layer
            palette = QtGui.QPalette()
            self.ui.txLayer.setPalette(palette)
            self.ui.txLayer.setText(layer.name())
            self.setItems(layer)
            # connect pushbutton to functions
            self.ui.pbnEdit.setEnabled(False)
            self.ui.pbnGenerate.clicked.connect(self.checkFieldInit)#createField)
            #self.ui.pbnGenerate.clicked.connect(self.initField)
            self.ui.pbnEdit.setEnabled(True)
            self.ui.pbnEdit.clicked.connect(self.point)
        elif (layer) and layer.type() != QgsMapLayer.VectorLayer:
            flag_vectorLayer = False
            palette = QtGui.QPalette()
            self.ui.txLayer.setPalette(palette)
            self.ui.txLayer.setText(layer.name())
            self.falseSet()
            infoString = unicode(" 1. " + "<font color='red'> Current layer is not a vector layer</font>")
            self.ui.lbStep1.setText(infoString)
        else:
            flag_vectorLayer = False
            self.falseSet()
            infoString = unicode("No layer selected... Select a layer from the layer panel")
            palette = QtGui.QPalette()
            palette.setColor(QtGui.QPalette.Text, QtCore.Qt.red)
            self.ui.txLayer.setPalette(palette)
            self.ui.txLayer.setText(infoString)
            
            
    def setItems(self, layer):
        vpr = layer.dataProvider()
        fields = vpr.fields()
        # show fields items for combobox
        for f in fields:
            self.ui.cbField.addItem(f.name())

     
    def falseSet(self):
        #self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        self.ui.buttonBox.button(QDialogButtonBox.Apply).setEnabled(False)
        #self.ui.txX.setEnabled(False)
        #self.ui.txY.setEnabled(False)
        self.ui.cbField.setEnabled(False)
        self.ui.pbnEdit.setEnabled(False)
        
        
    def trueSet(self):
        #self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
        self.ui.buttonBox.button(QDialogButtonBox.Apply).setEnabled(True)
        #self.ui.txX.setEnabled(False)
        #self.ui.txY.setEnabled(False)
        self.ui.cbField.setEnabled(True)
        self.ui.pbnEdit.setEnabled(True)
        
    
    def checkFieldInit(self):
        # set global variable
        global flag_create, flag_init, field_list
        
        # get current layer
        layer = self.iface.mapCanvas().currentLayer() # nF = layer.selectedFeatureCount() #print nF #self.ui.txX.setText("Yes, you can!")
        # get the field of current comobox
        cbField_origin = str(self.ui.cbField.currentText()) #print cbField_origin
        # prepare to access to layer data
        vpr = layer.dataProvider()
        # get fields and fileds' names
        fields = vpr.fields()
        field_names = [field.name() for field in fields]
        
        # add a Python list of QgsField objects, 
        # which defines the field name and type.
        lbHeader = cbField_origin[0:3]
        field_list =[
            [lbHeader + "|Field", QtCore.QVariant.String, "string", 64],
            [lbHeader + "|X", QtCore.QVariant.Double, "double", 13, 6],
            [lbHeader + "|Y", QtCore.QVariant.Double, "double", 13, 6],
            [lbHeader + "|Rot", QtCore.QVariant.Double, "double", 13, 6],
            [lbHeader + "|Size", QtCore.QVariant.Int, "integer",5],
            [lbHeader + "|AlignH", QtCore.QVariant.String, "string", 12],
            [lbHeader + "|AlignV", QtCore.QVariant.String, "string", 12],
            ]
        #print field_list #field_list[0][0]
        
        # loop to get flag_create
        for n in range(len(field_list)):
            #print field_list[n][0]
            flag_field_exist = field_list[n][0] in field_names
            #print field_list[n][0]
            # when field not exist and functionality supported flag_exe will be true
            #flag_exe = (flag_caps == True) and (not flag_field_exist == True)
            if (not flag_field_exist):
                flag_create = False
                break
            else:
                flag_create = True
                break
                
        # call function to create field and check whther to initialize fields        
        if (not flag_create):
            self.createField()
            flag_create = True
            flag_init = False
        else:
            flag_init = True
            """
            # check the first field value, to get flag_init
            allFeatures = layer.getFeatures()
            for feature in allFeatures:
                if (feature[field_list[1][0]] == 0.0]):
                    flag_init = True
                    break
                else:
                    flag_init = False
                    break
            """ 
        # decide initialization
        if (not flag_init):
            self.initField()
            flag_init = True
        
    
    def createField(self):        
        # get current layer
        layer = self.iface.mapCanvas().currentLayer() # nF = layer.selectedFeatureCount() #print nF #self.ui.txX.setText("Yes, you can!")
        # prepare to access to layer data
        vpr = layer.dataProvider()
        # get fields and fileds' names
        fields = vpr.fields()
        field_names = [field.name() for field in fields]
        
        # loop to create field
        for n in range(len(field_list)):
            #print field_list[n][0]
            flag_field_exist = field_list[n][0] in field_names
            if (not flag_field_exist):
                # add list to QgsField argument noting use *
                addField = QgsField(*field_list[n])
                # add field
                vpr.addAttributes([addField])
                # update the fields to complete the change
                layer.updateFields()
        
    
    def initField(self):    
        # get current layer
        layer = self.iface.mapCanvas().currentLayer() # nF = layer.selectedFeatureCount() #print nF #self.ui.txX.setText("Yes, you can!")
        vpr = layer.dataProvider()
        # Get the field of current comobox
        cbField_origin = str(self.ui.cbField.currentText()) #print cbField_origin
        
        # start to edit attributes of fields
        layer.startEditing()    
        allFeatures = layer.getFeatures()
        
        count = layer.featureCount()
        
        infoString = unicode("<font color='red'> Creating and initializing the label fields......Wait this completed please......</font>")
        progressMessageBar = self.iface.messageBar().createMessage(infoString)
        progress = QProgressBar()
        progress.setMaximum(count)
        progress.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        progressMessageBar.layout().addWidget(progress)
        self.iface.messageBar().pushWidget(progressMessageBar, self.iface.messageBar().INFO)
        
        # loop for initialization
        n = 0
        for feature in allFeatures:
            feature[field_list[0][0]] = feature[cbField_origin]
            feature[field_list[1][0]] = 0.0
            feature[field_list[2][0]] = 0.0
            feature[field_list[3][0]] = 0.0
            feature[field_list[4][0]] = 9
            feature[field_list[5][0]] = "Center"
            feature[field_list[6][0]] = "Half"
            
            n = n + 1
            layer.updateFeature(feature)   
            
            progress.setValue(n + 1)
        self.iface.messageBar().clearWidgets()

        
        # parameters for advanced labeling -- picked up from a qgs model file
        # generic labeling properties
        layer.setCustomProperty("labeling/fieldName", field_list[0][0])  #[0][0] )
        layer.setCustomProperty("labeling","pal" ) # new gen labeling activated
        layer.setCustomProperty("labeling/fontSize","9" ) # default value
        layer.setCustomProperty("labeling/multiLineLabels","true" ) # default value
        layer.setCustomProperty("labeling/enabled","true" ) # default value
        # layer.setCustomProperty("labeling/displayAll", "true") # force all labels to display
        layer.setCustomProperty("labeling/priority", "10") # puts a high priority to labeling layer
        layer.setCustomProperty("labeling/multilineAlign","1") # multiline align to center
        # layer.setCustomProperty("labeling/wrapChar", "%") # multiline break symbol
        # line properties case
        layer.setCustomProperty("labeling/placement","4" ) 
        
        # data defined properties
        layer.setCustomProperty("labeling/dataDefined/PositionX", "1~~0~~~~" + field_list[1][0])  
        layer.setCustomProperty("labeling/dataDefined/PositionY", "1~~0~~~~" + field_list[2][0])  
        layer.setCustomProperty("labeling/dataDefined/Rotation" ,"1~~0~~~~" + field_list[3][0])
        layer.setCustomProperty("labeling/dataDefined/Size" ,"1~~0~~~~" + field_list[4][0])
        layer.setCustomProperty("labeling/dataDefined/Hali", "1~~0~~~~" + field_list[5][0])  
        layer.setCustomProperty("labeling/dataDefined/Vali","1~~0~~~~" + field_list[6][0])  

        # updateExtents and refresh mapCanvas
        #layer.updateExtents()
        self.iface.mapCanvas().refresh()            
            
            
    def point(self):
        # setup QgsMapTool
        self.iface.mapCanvas().setMapTool(self.mapTool)
        self.mapTool.afterLeftClick.connect(self.showXY)
        if (flag_vectorLayer):
            self.mapTool.afterRightClick.connect(self.write)
        else:
            self.falseSet()
                
    
    def showXY(self):
        self.ui.txX.setText(str(share.xPosition))
        self.ui.txY.setText(str(share.yPosition))

       
    def write(self):

        # select the feature near the point
        # activates editing
        layer = self.iface.mapCanvas().currentLayer()
        self.iface.setActiveLayer(layer)
        layer.startEditing()
        
        # prepare to access to layer data
        vpr = layer.dataProvider()
        cbField_origin = str(self.ui.cbField.currentText())
        
        # add a Python list of QgsField objects, 
        # which defines the field name and type.
        lbHeader = cbField_origin[0:3]
        field_list =[
            [lbHeader + "|Field", QtCore.QVariant.String, "string", 64],
            [lbHeader + "|X", QtCore.QVariant.Double, "double", 13, 6],
            [lbHeader + "|Y", QtCore.QVariant.Double, "double", 13, 6],
            [lbHeader + "|Rot", QtCore.QVariant.Double, "double", 13, 6],
            [lbHeader + "|Size", QtCore.QVariant.Int, "integer",5],
            [lbHeader + "|AlignH", QtCore.QVariant.String, "string", 12],
            [lbHeader + "|AlignV", QtCore.QVariant.String, "string", 12],
            ]
        
        layer.setSelectedFeatures([share.found_featureID])
        # get x, y value from txX,txY qlineText and change them to attribute table
        try:
            # start to edit attributes of fields
            x = float(self.ui.txX.text()); #print x
            y = float(self.ui.txY.text()); #print y
            selectFet = layer.selectedFeatures()[0]
            # get the index of the fields you want to change
            indexX = layer.fieldNameIndex(field_list[1][0])
            indexY = layer.fieldNameIndex(field_list[2][0]) #print field_list[1][0], field_list[2][0]
            print indexX, indexY, selectFet.attributes(), selectFet.id()
            layer.changeAttributeValue(selectFet.id(), indexX, x)
            layer.changeAttributeValue(selectFet.id(), indexY, y)
            #layer.updateFeature(selectFet)
            #layer.commitChanges()
            layer.updateFields()
            self.iface.mapCanvas().refresh()
        except ValueError:
            QMessageBox.information(self, "Info", "Oops! get right coordinates first!", QtGui.QMessageBox.Ok)