##################################################################################
#
#   Module of QgsMapToolIdentify to make an interface between mouse and canvas
#
##################################################################################
from PyQt4.QtCore import pyqtSignal, Qt 
from qgis.core import QgsCoordinateReferenceSystem, QgsCoordinateTransform, QgsPoint
from qgis.gui import QgsMapToolIdentify
import qgis.utils
import share

class getCoordinate(QgsMapToolIdentify):
    afterLeftClick = pyqtSignal()
    afterRightClick = pyqtSignal()
    afterDoubleClick = pyqtSignal()
    
    
    def __init__(self, iface):
        QgsMapToolIdentify.__init__(self, iface.mapCanvas())
        self.iface = iface
    
    """
    def canvasPressEvent(self, event):
        x = event.pos().x()
        y = event.pos().y()
        transform = self.iface.mapCanvas().getCoordinateTransform()
        startPt = transform.toMapCoordinates(x, y)
        print "start", startPt
    """
        
        
    def canvasReleaseEvent(self, event):
        if (event.button() == Qt.LeftButton):
            # crs operation preparation
            crsSrc = self.iface.mapCanvas().mapRenderer().destinationCrs() # mapCanvas crs
            crsCode = qgis.utils.iface.activeLayer().crs().authid() # get active layer's crs code
            crsLayer = QgsCoordinateReferenceSystem(crsCode) # active layer's crs            
            # get x, y coordinate which is integer; you can also use x = event.x()
            x = event.pos().x() #print x
            y = event.pos().y()
            transform = self.iface.mapCanvas().getCoordinateTransform()
            self.endPt = transform.toMapCoordinates(x, y) #print self.endPt            
            # crs operation
            crsTransform = QgsCoordinateTransform(crsSrc, crsLayer)
            self.endPt = crsTransform.transform(QgsPoint(self.endPt.x(),self.endPt.y()))
            
            # assign the clicked point's coordinates to variable in share
            share.xPosition = round(self.endPt.x(),3)
            share.yPosition = round(self.endPt.y(),3)
            
            # clear previous selection when starting next selection
            currentLayer = self.iface.mapCanvas().currentLayer()
            currentLayer.removeSelection()
            
            # Identify the feature near the point and send feature id to share's variable
            idf = self
            found_features = idf.identify(x, y, idf.ActiveLayer, idf.VectorLayer)
            #found_features = idf.identify(x, y, idf.TopDownStopAtFirst, idf.VectorLayer)
            if len(found_features) > 0:
                layer = found_features[0].mLayer
                feature = found_features[0].mFeature
                share.found_featureLayername = layer.name()
                share.found_featureID = feature.id(); # print share.found_featureID
                layer.setSelectedFeatures([share.found_featureID])
                
            #send signal
            self.afterLeftClick.emit()
        if (event.button() == Qt.RightButton):
            pass
            # send signal
            #self.afterRightClick.emit() # reserve this for further development
            
            
    def canvasDoubleClickEvent(self, event):
        self.afterDoubleClick.emit()
