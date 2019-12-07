# Setting up gloves in Motionbuilder

# 1. Downloading Motionbuilder

You can download the latest Motionbuilder from [here](https://www.arduino.cc/download_handler.php?f=https://www.microsoft.com/store/apps/9nblggh4rsd8?ocid=badge). And download is complete
just following on-screen instructions.

# 2. Glove setup

### 2.1 Driver installation


*  Copy the file **ordevice5dt16.dll** and **fglove.dll** to the *C:\[Program File]\Autodesk\Motionbuilder\bin\win32\plugins\* directory.
*  Run Motiobuilder
*  Confirm that the driver is installed by viewing the 5DT device template is in the asset browser (as seen in Figure 1 below).

![Figure 1](https://cseegit.essex.ac.uk/ce301_2019/ce301_willock_j/blob/master/Technical%20Documentation/Getting%20Started%20(Software)/images/assetBrowser_5DTsnip.png)

### 2.2 Opening Glove

From the asset browser, click on the 5DT DataGlove device. Then drag and drop into the viewer scene.

This will open up the navigator pane as seen below (Figure 2)

![Figure 2](https://cseegit.essex.ac.uk/ce301_2019/ce301_willock_j/blob/master/Technical%20Documentation/Getting%20Started%20(Software)/images/GloveNaviSetup.png)

1.  If the port is not already selected press **Rescan Ports** to find the correct port.
2.  Create model binding **5DTGlove1:hand**.
3.  Click **Online** once the previous steps are complete.

# 3. Connecting to an actor

Go back to the asset browser and go to the Characters Pane.

Drag and drop the **Actor** character into the viewer pane.

You can then create a **MarkerSet**. Once a MarkerSet has been created, drag and drop the root glove device (located in the scene drop down menu), it should be called **5DTGlove1:hand**.

**NOTE: The glove will only for 2 minutes at a time in demo mode**
