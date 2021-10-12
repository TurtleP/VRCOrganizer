## VRCOrganizer

A simple python script to reorganize VRChat photos. The recent Closed Beta (10/08/2021) updated the Camera System. This also enforces organization, which honestly is a good thing. **_New_** photos are stored in a directory under `Photos/VRChat/YYYY-MM` . However, since this does not reflect on **_old_** ones, this is going to fix that.

Some people don't like this organization, but realistically I think it's great. They should, however, add a config option for this (and I believe someone has opened feedback on it by now to do so).

Regardless, just download the executable file from the releases page, place it in your VRChat photos directory, and run it. If you try to run it in any other directory, it will simply give an alert popup to tell you to run it in the proper directory.

### How it Works

The script will scan the directory for *all* photos within this top-level directory. Nothing further in. Once it has this information, the script then determines what year and month it belongs in. It does this by checking the filename first since they do contain the date they were taken.

However, if the filename fails to determine something, it uses the creation time. This should be accurate enough 99% of the time, but if the file was *copied* at all, the creation time will change. There is a failsafe for that, which is just checking the modification time instead. Thing is, I don't think it really works well and the first two scenarios are more likely to work properly anyway.

In order to preserve all this data, it does a *move* operation instead of a *copy*. Slightly risky, for technical reasons, but it does preserve the creation and modification times. Otherwise it would only preserve the modification and access times. If there's an issue with this, I can change it to simply use the copy method so it is safer than moving.
