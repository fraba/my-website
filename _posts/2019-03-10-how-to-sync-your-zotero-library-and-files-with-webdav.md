---
title: "How to sync your Zotero library (and files) with WebDAV"
date: "2019-03-10"
categories: 
  - "how-to"
tags: 
  - "cloudstor"
  - "how-to"
  - "sync"
  - "webdav"
  - "zotero"
---

In this post, I explain how to use an online file storing and sharing service like AARNet's CloudStor (but any WebDAV service will do) to access and update your Zotero library from different computers.

Zotero is the best reference management software that you can use. The main reasons are:

- It's free (like in _free beer_);
- It's free (like in _free speech_).
- Zotero is available for Mac, Windows and Linux.

Also,

- Zotero is developed by a large and active community of developers.

That is,

- It's very stable and constantly improving;
- It comes with a huge library of _translators_ to easily import to your library and plugins to export from your library (e.g. to Word or to LaTex).

For the purpose of this post, let's consider your Zotero library, which you manage through the Zotero app, as a collection of items. An item can be a journal article, a book, a website, or a movie. (Or whatever you need to reference). Each item comes with a bunch of _metadata_ – information about authors, publication date, journal name, etc. – but also with a _link to the actual file_ of the document that you have saved on your computer.

Now, if you want to share your library across multiple computers (or if you just want to back up your library online), Zotero offers you two options.

1. You can host your library on Zotero.org's servers (free under 300MB, you pay above);
2. You can host your library on other servers that allow access via [WebDAV.](https://en.wikipedia.org/wiki/WebDAV)

If your server runs [ownCloud](https://en.wikipedia.org/wiki/OwnCloud), you are good as ownCloud supports WebDAV. Syncing is actually pretty simple. You will need to know

1. the URL address you need to access your files via WebDAV, and
2. the corresponding username and password.

## AARNet's Cloudstor settings (March 2019)

If you happen to use [CloudStor](https://support.aarnet.edu.au/hc/en-us/categories/200217608-CloudStor), [AARNet](https://www.aarnet.edu.au/)'s file sync service, your URL will be `https://cloudstor.aarnet.edu.au/plus/remote.php/webdav/`. Your username and password are different from what you use to access the service. Indeed, you will need to create a password for a new app by navigating "settings" (in the top-right corner drop-down menu) -> "security" -> "create new app password". And it is probably a good idea to have a different app password for every computer you want to sync with your Zotero library.

Once you have your password (your username should be your university email address), go to Zotero's settings (or preferences). Under the "sync" tab,

1. Enter your Zotero account credentials. Importantly, you will need to have a Zotero.org account even if you store your files using WebDAV and link your Zotero app on every computer you use to it.
2. Enter the WebDAV URL, your username and your password and click on "Verify Server to check that everything is right".

These are my settings:

\[caption id="attachment\_1162" align="aligncenter" width="909"\][![](images/Screen-Shot-2019-03-10-at-6.40.50-pm-909x1024.png)](http://www.francescobailo.net/wordpress/wp-content/uploads/2019/03/Screen-Shot-2019-03-10-at-6.40.50-pm.png) Settings to sync my Zotero library via WebDAV and CloudStor.\[/caption\]

## My setting and workflow

I read articles and books from my Zotero library on my iPad with the [GoodReader app](http://www.goodreader.com/). GoodReader on top of being an excellent reader [can also sync](http://www.goodreader.com/gr-man-tr-servers.html) with multiple file storage and synchronization services (e.g. DropBox or Google Drive). I use [ZotFile](http://zotfile.com/), a Zotero plugin, to rename Zotero files, mostly PDFs but also a few EPUBs or HTML pages, and store them locally anywhere I want.

### My old setting and workflow

Before syncing my library via WebDAV and share it with multiple computers (in my case, office desktop and laptop), I used [ZotFile](http://zotfile.com/) to rename my Zotero files based on a consistent file naming rule and to move them in a local folder within my Google Drive folder. Google Drive allowed to access all my files and read them on my iPad. In fact, I set GoodReader to download locally on the iPad every file in the Google Drive folder. So my workflow looked like this:

1. I added items to the Zotero library from my laptop and used to ZotFile to rename and move the files to my Google Drive;
2. I could access Zotero files both from my laptop and from the iPad. In both cases, I could edit the PDFs with highlights and comments and share them across the two devices.

### My new setting and workflow

As I decided to use WebDAV, I can't use ZotFile to store files in a "custom folder" (Google Drive in my case). I can still rename files, but I need to keep them within the default Zotero directory structure to allow syncing. This is crucial: Zotero will sync via WebDAV only files respecting Zotero default storing rules.

\[caption id="attachment\_1166" align="aligncenter" width="1024"\][![](images/Screen-Shot-2019-03-11-at-9.01.08-am-1024x438.png)](http://www.francescobailo.net/wordpress/wp-content/uploads/2019/03/Screen-Shot-2019-03-11-at-9.01.08-am.png) ZotFile settings while using WebDAV.\[/caption\]

So this is my new workflow:

1. I add items to the Zotero library from my laptop and used to ZotFile to rename files;
2. Files are clearly still accessible from my laptop (and now also from my desktop). But if I want to read them on my iPad with GoodReader, I need to use another function implemented by ZotFile: I can set ZotFile so that by right-clicking on any item or file from within Zotero I can send it to the tablet (where I can edit it) and when I finish reading get it back from the tablet.

\[caption id="attachment\_1167" align="aligncenter" width="990"\][![](images/Screen-Shot-2019-03-11-at-9.30.42-am.png)](http://www.francescobailo.net/wordpress/wp-content/uploads/2019/03/Screen-Shot-2019-03-11-at-9.30.42-am.png) ZotFile: Send file to the tablet.\[/caption\]

And these are my settings for ZotFile:

\[caption id="attachment\_1168" align="aligncenter" width="1024"\][![](images/Screen-Shot-2019-03-11-at-9.30.08-am-1024x1012.png)](http://www.francescobailo.net/wordpress/wp-content/uploads/2019/03/Screen-Shot-2019-03-11-at-9.30.08-am.png) ZotFile settings to share files with a tablet.\[/caption\]

## Support Zotero and ZotFile development

These settings will allow you to use a cloud syncing service you already have without any extra charge. Still, as a user of Zotero and ZotFile (which are free), it is fair to contribute financially to the projects.

As far as I know, there is no direct way to contribute to Zotero directly but [you can make a donation](https://advancement.gmu.edu/ihm02) to the  Roy Rosenzweig Center for History and New Media, which initiated the project, or [upgrade](https://www.zotero.org/settings/storage) your storage plan.

You can make a donation to ZotFile from the [project homepage](http://zotfile.com/).
