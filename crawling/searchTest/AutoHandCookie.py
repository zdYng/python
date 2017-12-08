# -*- coding:utf-8 -*-

import os
import cookielib
import urllib2

def AutoHandleCookie():
    cookieJarMemory = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJarMemory))
    urllib2.install_opener(opener)

    demoUrl ="http://www.baidu.com"
    response = urllib2.urlopen(demoUrl)

    cookieFilenameLWP = "localCookiesLMP.txt"
    cookieJarFileLWP = cookielib.LWPCookieJar(cookieFilenameLWP)
    cookieJarFileLWP.save()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJarFileLWP))
    urllib2.install_opener(opener)

    demoUrl = "http://www.baidu.com"
    response = urllib2.urlopen(demoUrl)
    cookieJarFileLWP.save()


    cookieFilenameMozilla = "localCookiesMozilla.txt"
    cookieJarFileMozilla = cookielib.MozillaCookieJar(cookieFilenameMozilla)
    cookieJarFileMozilla.save()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJarFileMozilla))
    urllib2.install_opener(opener)

    demoUrl ="http://www.baidu.com"
    response = urllib2.urlopen(demoUrl)
    cookieJarFileMozilla.save()

    parseAndSavedCookieFile = "parseAndSaveCookies.txt"
    parseCookieJarFile =  cookielib.MozillaCookieJar(parseAndSavedCookieFile)
    print parseCookieJarFile
    parseCookieJarFile.load(cookieFilenameMozilla)
    print parseCookieJarFile

if __name__ =="__main__":
    AutoHandleCookie()