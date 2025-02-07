import time

class AggregatedReader():

    def __init__(self, engine="dynamsoft"):
        self.reader = None
        self.engine = engine
        self.init_reader()
        
    def init_reader(self):
        if self.engine == "dynamsoft" or self.engine == "":
            from barcode_reader.dynamsoft import DynamsoftBarcodeReader
            self.reader = DynamsoftBarcodeReader()
        elif self.engine == "DBR 8.8":
            from barcode_reader.commandline import CommandLineBarcodeReader
            self.reader = CommandLineBarcodeReader(port=6666,config_path="dbr88_commandline")
        elif self.engine == "commandline":
            from barcode_reader.commandline import CommandLineBarcodeReader
            self.reader = CommandLineBarcodeReader()
        elif self.engine == "scandit":
            from barcode_reader.commandline import CommandLineBarcodeReader
            self.reader = CommandLineBarcodeReader()
        elif self.engine == "accusoft":
            from barcode_reader.commandline import CommandLineBarcodeReader
            self.reader = CommandLineBarcodeReader(port=5558,config_path="accusoft_commandline")
        elif self.engine == "aspose":
            from barcode_reader.aspose import AsposeBarcodeReader
            self.reader = AsposeBarcodeReader()
        elif self.engine == "zxing":
            from barcode_reader.commandline import CommandLineBarcodeReader
            self.reader = CommandLineBarcodeReader(port=5557,config_path="zxing_commandline")
        elif self.engine == "zxingcpp":
            from barcode_reader.zxingcpp import ZXingBarcodeReader
            self.reader = ZXingBarcodeReader()
        elif self.engine == "zbar":
            from barcode_reader.zbar import ZbarBarcodeReader
            self.reader = ZbarBarcodeReader()
        elif self.engine == "ean13":
            from barcode_reader.ean13 import EAN13Reader
            self.reader = EAN13Reader()
        elif self.engine == "opencv1d":
            from barcode_reader.opencv1d import OpenCV1DReader
            self.reader = OpenCV1DReader()
        elif self.engine == "boofcv":
            from barcode_reader.boofcv import BoofCVReader
            self.reader = BoofCVReader()
        elif self.engine == "opencv_wechat":
            from barcode_reader.opencv_wechat_qrcode import OpenCVWechatQrReader
            self.reader = OpenCVWechatQrReader()
        elif self.engine == "ML Kit":
            from barcode_reader.http_barcodereader import HTTPBarcodeReader
            self.reader = HTTPBarcodeReader(sdk="MLKit")
        elif self.engine == "Apple Vision":
            from barcode_reader.http_barcodereader import HTTPBarcodeReader
            self.reader = HTTPBarcodeReader(sdk="AppleVision")
        elif self.engine == "Scandit 6.x":
            from barcode_reader.http_barcodereader import HTTPBarcodeReader
            self.reader = HTTPBarcodeReader(sdk="Scandit")
        elif self.engine == "DBR (iOS)":
            from barcode_reader.http_barcodereader import HTTPBarcodeReader
            self.reader = HTTPBarcodeReader(sdk="DBR")
        elif self.engine == "ZXingObjC":
            from barcode_reader.http_barcodereader import HTTPBarcodeReader
            self.reader = HTTPBarcodeReader(sdk="ZXing")
        elif self.engine == "Object Detector":
            from barcode_reader.object_detection import ObjectDetector
            self.reader = ObjectDetector()
        elif self.engine == "YOLODBR":
            from barcode_reader.yolo_dbr import YOLODBR
            self.reader = YOLODBR()
        elif self.engine == "libdmtx":
            from barcode_reader.libdmtx import DMTX
            self.reader = DMTX()    
            
    
    def decode_file(self, file_path,settings=""):
        if settings!="":
            try:
                self.reader.set_runtime_settings_with_template(settings)
            except:
                print("wrong settings")
        start_time = time.time()
        results = self.reader.decode_file(file_path)
        end_time = time.time()
        elapsedTime = int((end_time - start_time) * 1000)
        if "elapsedTime" not in results:
            results["elapsedTime"] = elapsedTime
        return results
        