deviceid = "192.168.56.102:5555"
adbikili = "/usr/bin/adb"
crashids = [b"SIGSEGV" , b"SIGFPE" , b"SIGILL" , b"sigsegv" , b"sigfpe" , b"sigill", b"crash", b"CRASH"]
bekle = 0.3
debug = False
pdf_okuyucular = ["com.google.android.apps.pdfviewer"]
pdf_o_args = {
        "google": ["am", "start", "-a", "android.intent.action.VIEW", "-n", "com.google.android.apps.pdfviewer/com.google.android.apps.viewer.PdfViewerActivity","-t", "application/pdf", "-d"]

}

