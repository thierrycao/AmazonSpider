import platform

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import random

from bs4 import BeautifulSoup
import requests
import os
import codecs
import xlrd
import xlwt
import re

import pickle
import shutil

from PyQt5 import QtWidgets

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, QtCore


class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration

    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args:  # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False

class amazon_stock(QObject):
    _trigger_int = pyqtSignal(int)
    _trigger_str = pyqtSignal(str)
    _trigger_list = pyqtSignal(list)
    _trigger_dict = pyqtSignal(dict)
    _trigger_progress = pyqtSignal(int,int,int)

    def __init__(self):
        super(amazon_stock,self).__init__()
        self.setupData()

    def setup(self):

        ##prepare File and Document Struct
        if not self.prepare_Struct():
            return

        ##import Pickle which is backup data for quick generate data
        if not self.import_PickleData():
            return

    def setupData(self):
        self.waitingReadUserChoose = ''
        self.nowDate = time.strftime('_%Y_%m_%d', time.localtime())
        self.productInstance = {'num': 0, 'list': []}
        self.mQueue = ''

    def start_real(self):
        self.amazon_print('hello world!')
    
    def start(self):
        self.setup()
        self.amazon_print(self.productInstance)
        
        for key,value in enumerate(self.productInstance['list']):
            if value['data']:
                continue
            self.amazon_print(key)
            self.browser_htmls(key)
            self.amazon_print("hhhhh")
        time.sleep(10)
        ##save the list data in Xlsx
        self.save_xl()
    

    def startCrawl(self,url):
        ##
        self.amazon_print('start crawl')
        print('start crawl')


    def amazon_get_url(self,url):
        """
        driver.implicitly_wait(4) # 隐性等待，
        driver.get(url) # Load page
        if driver.find_element_by_xpath("//span[@id='submit.add-to-cart-announce']").is_displayed():
            return True
            
        """
        print(11)
        #submit.add-to-cart-announce

    def amazon_distribute_url2spider(self,url):
        
        #urlList = []
        #jsList = [ 'window.open("%s")'%i for i in urlList ]
        """
        for i in jsList:
            driver.excute_script(i)
        """
        driver = self.driver

        js = 'window.open("%s")'%url
        #execute js script to add an new tabPage
        driver.execute_script(js)
        window_tables = driver.window_handles

        #focus on the object window to scratch data
        driver.switch_to_window(driver.window_handles[-1])

        realtext = self.amazon_getText_review(driver)

        #close the temporary Task window and focus on the Auxiliary window 'Our Dear Baidu' 
        driver.close()
        driver.switch_to_window(driver.window_handles[-1])
        
        self.driver = driver
        return realtext


 

    def amazon_getText_review(self,driver):
        
        
        #driver.implicitly_wait(4) # 隐性等待，最长等30秒
        #driver.get(url) # Load page
        #self.amazon_get_url(driver,url)
        

        unAvailableKeyString = ['reservadas','unavailable','Claimed','vendus','non disponibile','richiesto']

        while (1):
            try:
                hh = driver.find_element_by_xpath("//input[@id='add-to-cart-button' and @name='submit.add-to-cart']")
                hh.click()
                break
            except:
                time.sleep(1)
                self.amazon_print("unavailable now------------")

                try:
                    needContinue = driver.find_element_by_xpath("//input[@alt='Continuar' and @value='addToCart' and @name='submit.addToCart']")
                    self.amazon_print(needContinue.text)
                    needContinue.click()

                except:
                    pass

                try:
                    isAvailable = driver.find_element_by_xpath("//div[@id='availability']").text
                    isAvailableList = driver.find_element_by_xpath("//div[@id='availability']")
                    self.amazon_print(isAvailable)
                    if 'these sellers' in isAvailable:
                        #otherSellers_url=isAvailableList.find_element_by_css_selector('a').get_attribute('href')
                        #otherSellers_url.clicked()
                        return '0'

                    for i in unAvailableKeyString:
                        if i in isAvailable:
                            self.amazon_print(isAvailable)
                            return '0'
                except:
                    pass

                try:
                    isAvailable = driver.find_element_by_xpath("//div[@id='deal_availability']").text
                    for i in unAvailableKeyString:
                        if i in isAvailable:
                            self.amazon_print(isAvailable)
                            return '0'
                except:
                    pass




                continue

        time.sleep(2)
        while (1):
            try:
                #cc = driver.find_element_by_class_name('a-button-text')
                cc = driver.find_element_by_xpath("//span[@id='hlb-view-cart' and @class='a-button huc-v2-view-cart huc-spacing-right-mini huc-button-large']")
                privious_pageUrl = driver.current_url
                # print(privious_pageUrl)
                cc.click()
                time.sleep(2)
                forward_pageUrl = driver.current_url
                # print(forward_pageUrl)
                while (privious_pageUrl == forward_pageUrl):
                    cc.click()
                    time.sleep(2)
                    forward_pageUrl = driver.current_url

                break;
            except:
                time.sleep(1)
                continue

        time.sleep(3)

        while (1):
            try:
                dd = driver.find_element_by_id('dropdown1_9')
                dd.click()
                break;
            except:

                while (1):
                    try:
                        dd_a = driver.find_element_by_xpath("//span[@class='a-button-text a-declarative']")
                        dd_a.click()
                        break;
                    except:
                        time.sleep(1)
                        continue
                time.sleep(1)
                continue

        # dd_a.send_keys("999" + Keys.RETURN)
        ##
        # 拖动控件 显示10+
        time.sleep(2)
        while (1):
            try:
                ee = driver.find_element_by_name('quantityBox')
                ee = driver.find_element_by_css_selector("input[name=\"quantityBox\"]")
                time.sleep(1)
                ee.send_keys("999" + Keys.RETURN)
                break
            except:
                time.sleep(1)

                continue

        time.sleep(2)
        while (1):
            try:
                ff = driver.find_element_by_xpath("//div[@class='sc-quantity-update-message a-spacing-top-mini']")
                mytext = ff.text
                break;
            except:
                time.sleep(1)
                continue

        # invoice=driver.find_element_by_xpath("//span[@class='a-size-medium #a-text-bold']")

        self.amazon_print(mytext)
        pattern = re.compile(r'\D')
        realtext = pattern.sub(r'', mytext)
        self.driver = driver




        # delete the Redundant

        shopBaseket = driver.find_elements_by_xpath(
            "//div[@class='a-row sc-list-item sc-list-item-border sc-java-remote-feature']")

        value = shopBaseket[-1]
        if not self.deleteIT(value):
            self.amazon_print('not found IT delete')
            if not self.deleteES(value):
                self.amazon_print('not found ES delete')
                if not self.deleteFR(value):
                    self.amazon_print('not found FR delete')
                    if not self.deleteEG(value):
                        self.amazon_print('not found EG delete')
        time.sleep(2)
        
        
        return realtext
    
    def deleteES(self,value):
        try:
            Eliminar = value.find_element_by_xpath("//input[@value='Eliminar']")
            Eliminar_text = Eliminar.get_attribute('aria-label')
            self.amazon_print('ES allready deleted!')
            Eliminar.click()
        except:
            return 0
        
    def deleteEG(self,value):
        try:
            Delete = value.find_element_by_xpath("//input[@value='Delete']")
            Delete_text = Delete.get_attribute('aria-label')
            self.amazon_print('EG allready deleted!')
            Delete.click()
        except:
            return 0
    def deleteFR(self,value):
        
        try:
            Supprimer = value.find_element_by_xpath("//input[@value='Supprimer']")
            Supprimer_text = Supprimer.get_attribute('aria-label')
            self.amazon_print('FR allready deleted!')
            Supprimer.click()
        except:
            return 0
    def deleteIT(self,value):
        try:
            Rimuovi = value.find_element_by_xpath("//input[@value='Rimuovi']")
            Rimuovi_text = Rimuovi.get_attribute('aria-label')
            self.amazon_print('IT allready deleted!')
            Rimuovi.click()
        except:
            return 0
        
		

    def save_text(self,file_name,text):


        with codecs.open(file_name,'wb',encoding = 'utf-8') as fp:
            ##codecs 文件操作模块
            try:
                #path = os.path
                for p in text:
                    fp.write('%s\t\t%s\t\t%s\t\t%s\r\n'%(p['name'],p['asin'],p['site'],p['stock']))
                    """
                    if isinstance(p,list):
                        for i in p:
                            fp.write('\t%s\t\r\n'%i)
                    else:
                        fp.write('\t%s\t\r\n'%p)
                        """
            except IOError as err:
                print('IOError ' + str(err))
            self.amazon_print('Read finish!')
        return




    '''
    设置单元格样式
    '''

    def set_style(self,name,height,bold=False):
        style = xlwt.XFStyle() # 初始化样式

        font = xlwt.Font() # 为样式创建字体
        font.name = name # 'Times New Roman'
        font.bold = bold
        font.color_index = 4
        font.height = height

        # borders= xlwt.Borders()
        # borders.left= 6
        # borders.right= 6
        # borders.top= 6
        # borders.bottom= 6

        style.font = font
        # style.borders = borders

        return style

    def save_xl(self):

        default_FileName = self.resDic['generate']['xlsx_0']

        f = xlwt.Workbook() #创建工作簿

        (sheet1_data,sheet2_data) = list(map(lambda x:x['data'],self.productInstance['list']))

        row0 = [u'name',u'site',u'asin',u'stock']




        if sheet1_data:
            sheet1 = f.add_sheet(u'banzi',cell_overwrite_ok=True) #创建sheet1
            #生成第一行
            ##sheet1
            for i in range(0,len(row0)):
                sheet1.write(0,i,row0[i],self.set_style('Times New Roman',220,True))

            for i in range(0,len(sheet1_data)):
                temp_data=[sheet1_data[i]['name'],sheet1_data[i]['site'],sheet1_data[i]['asin'],sheet1_data[i]['stock']]
                for j in range(0,len(row0)):
                    sheet1.write(i+1,j,temp_data[j],self.set_style('Times New Roman',220,True))

        if sheet2_data:
            sheet2 = f.add_sheet(u'ping',cell_overwrite_ok=True) #创建sheet2
            ##sheet2
            for i in range(0,len(row0)):
                sheet2.write(0,i,row0[i],self.set_style('Times New Roman',220,True))

            for i in range(0,len(sheet2_data)):
                temp_data=[sheet2_data[i]['name'],sheet2_data[i]['site'],sheet2_data[i]['asin'],sheet2_data[i]['stock']]
                for j in range(0,len(row0)):
                    sheet2.write(i+1,j,temp_data[j],self.set_style('Times New Roman',220,True))

        #生成第一列
        """
        for i in range(0,len(column0)):
            sheet1.write(i+1,0,column0[i],self.set_style('Times New Roman',220))
        
        
        sheet1.write(1,2,'1991/11/11')
        sheet1.write_merge(7,7,2,4,u'暂无') #合并列单元格
        sheet1.write_merge(1,2,4,4,u'好朋友') #合并行单元格
        """

        f.save(default_FileName) #保存文件
        self.amazon_print("save_xl as :%s successful"%default_FileName)

    def save_pickle(self,pickle_name,products):

        try:
            with open(pickle_name,'wb') as pp:
                pickle.dump(products,pp)
        except IOError as error:
            print("pickle dump IOError" + error)
            return

        self.amazon_print("save_pickle as :%s successful!"%(pickle_name))

    def getWorkBookData(self,index):
        resDic = self.resDic
        document = resDic['source']['waitingReadXlsx']

        try:
            data = xlrd.open_workbook(document)
        except IOError as err:
            print("Error: cause by read workbook" + str(err))
            return

        v = index
        for case in switch(v):
            if case(0):
                self.amazon_print('index:%s'%v)
                file_name = 'banzi'
                text_name = resDic['generate']['text'][v]  ##文件名
                file_pikle = resDic['temp']['pickle'][v]['name']

                try:
                    table = data.sheet_by_name(r'banzi')
                except:
                    print("Not found pointed sheet %s in document"%file_name)
                    return

                break
            if case(1):
                self.amazon_print('index:%s'%v)
                file_name = 'ping'
                text_name = resDic['generate']['text'][v]   ##文件名
                file_pikle = resDic['temp']['pickle'][v]['name']

                try:
                    table = data.sheet_by_name(r'ping')
                except:
                    print("Not found pointed sheet %s in document"%file_name)
                    return

                break
            if case(): # 默认
                self.amazon_print('something else!')
                return

        return (text_name,file_pikle,table)


    def browser_htmls(self,index):

        ##Get WorkBook data
        if not self.getWorkBookData(index):
            return

        (text_name,file_pikle,table) = self.getWorkBookData(index)


        ##Begin grab htlms from
        driver = webdriver.Firefox() # Get local session of firefox
        driver.get('http://www.baidu.com')
        self.driver = driver
        #driver = webdriver.PhantomJS(executable_path='/mnt/.md/.ff/.ps/temp/11/python3/tools/phantomjs-2.1.1-linux-x86_64/bin/phantomjs') # Get local session of firefox
        nrows = table.nrows

        htmls = []
        products=[]



        num = 0
        for i in range(nrows):
                if i == 0 or i== 1:
                    continue
                if table.row_values(i)[6].strip() == '':
                    break

                #add new one
                products.append({'name':'','site':'','asin':'','stock':''})

                if table.row_values(i)[1].strip() == '':
                    products[num]['name'] = products[num-1]['name']
                    #continue
                else:
                    products[num]['name'] = table.row_values(i)[1]

                products[num]['asin'] = table.row_values(i)[2]
                products[num]['site'] = table.row_values(i)[3]


                self.amazon_print(products[num])

                num = num + 1
                htmls.append(table.row_values(i)[6])

        #self._trigger_step1.emit(index,len(htmls))



        #url = 'https://www.amazon.es/dp/B00N503MXO?m=ASUJFHEZDFK07&ref_=v_sp_detail_page'
        num = 0
        for i in htmls:


            products[num]['stock'] = self.amazon_distribute_url2spider(i)
            self.amazon_print(products[num])
            if products[num]['stock'] == '':
                products[num]['stock'] = self.amazon_distribute_url2spider(i)

            num = num + 1

            self.amazon_progree(index,len(htmls),num)
            #self._trigger_progress.emit(index,len(htmls),num)

            #print(rv)

        ##save list data in pickle
        self.save_pickle(file_pikle,products)


        ##save list data in text
        self.save_text(text_name,products)

        self.productInstance['list'][index]['data'] = products
        #return products


    def pathJoin_machine(self,file_name):
        resource_Dir = 'res\\'
        return resource_Dir + file_name

    def amazon_print(self,msg):
        self._trigger.emit(msg)

    def import_PickleData(self):
        self.amazon_print(self.waitingReadUserChoose)
        products = {'num':0,'list':[]}
        for key,value in enumerate(self.resDic['temp']['pickle']):
            products['list'].append({'name':'','data':''})
            try:
                with open(value['name'],'rb') as pp:
                    product = pickle.load(pp)
                    products['list'][key]['data'] = product

            except IOError as err:
                print('pickle read err,cause by IOError' + str(err))
                pass
            finally:
                products['list'][key]['name'] = self.resDic['temp']['pickle'][key]['item']
                products['num'] += 1

        if not products:
            self.amazon_print('Pickle list\'s raw data is Null!')
            print('Pickle list\'s raw data is Null!')
        self.productInstance = products
        return products

        """    
        
        for i in range(len(self.resDic['temp'])):
            if i == 0:
                file_name_board = self.resDic['temp']['pickle'][i]
            if i == 1:
                file_name_lcd = self.resDic['temp']['pickle'][i]

        default_pickle_A = file_name_board
        default_pickle_B = file_name_lcd
        
        product_A = []
        product_B = []

        try:
            with open(default_pickle_A,'rb') as bp:
                product_A = pickle.load(bp)
            with open(default_pickle_B,'rb') as pp:
                product_B = pickle.load(pp)

        except IOError as err:
            print('pickle read err,cause by IOError' + str(err))
            pass
        
        #print(product_A,product_B)
        return product_A,product_B
        """

    def search_fileOrdir(self,file_name, search_path = os.getcwd(), index = 'file', pathsep = os.pathsep):
        for path in search_path.split(pathsep):
            candidate = os.path.join(path, file_name)
            if index == 'file':
                if os.path.isfile(candidate):
                    return os.path.abspath(candidate)
            if index == 'dir':
                if os.path.isdir(candidate):
                    return os.path.abspath(candidate)
        return None

    def prepare_Struct(self):

        currentPath = os.getcwd()
        currentPlatformSystem = platform.system()

        self.amazon_print(self.waitingReadUserChoose)
        waitingReadUserChoose = os.path.basename(self.waitingReadUserChoose)

        nowDate = self.nowDate
        thisTimeDate = time.strftime('%Y_%m_%d', time.localtime())


        for case in switch(currentPlatformSystem):
            if case('Windows'):
                resPath = currentPath + '\\res\\' + thisTimeDate + '\\'
                resDic = {'local':{'path':resPath},              \
                          'source':{'path':resPath + 'source\\'},\
                          'temp':{'path':resPath + 'pickle\\'},\
                          'generate':{'path':resPath + 'generate\\'}}
                break;
            if case('Linux'):
                resPath = currentPath + '/res/' + thisTimeDate + '/'
                resDic = {'local': {'path': resPath}, \
                          'source': {'path': resPath + 'source/'}, \
                          'temp': {'path': resPath + 'pickle/'}, \
                          'generate': {'path': resPath + 'generate/'}}
                break;
            if case():
                self.amazon_print('Other unsupport platform, exit')
                print('Other unsupport platform, exit')
                return

        #key file
        waitingReadBacXlsx = 'amazon_stock.xlsx'
        waitingReadXlsx = 'amazon_stock.xlsx'
        waitingReadRealTimeXlsx = 'amazon_stock_rawdata' + nowDate + '.xlsx'
		#waitingReadBacXlsx = 'amazon_stock.xlsx'
		#waitingReadRealTimeXlsx = 'amazon_stock_rawdata' + nowDate + '.xlsx'
		#waitingReadUserChoose = self.waitingReadUserChoose
        waitingReadXlsxDic = {'waitingReadBacXlsx':{'name':waitingReadBacXlsx,'isExist' : True},\
                       'waitingReadRealTimeXlsx' : {'name':waitingReadRealTimeXlsx,'isExist' : True },\
					   'waitingReadUserChoose':{'name':waitingReadUserChoose, \
					   'isExist': (waitingReadUserChoose == '')} \
							  }

        mainItems = ['banzi','ping']

        #temp file
        list_pickle = [ value + nowDate + '.pickle' for value in mainItems ]

        #generate file
        saved_XlsxName = 'amazon_stock' + nowDate + '.xlsx'
        saved_textName = [ value + nowDate + '.txt' for value in mainItems ]

        ##Create Dir Struct
        for i in resDic:
            if not os.path.exists(resDic[i]['path']):
                os.makedirs(resDic[i]['path'])

        waitingReadXlsx = waitingReadXlsxDic['waitingReadUserChoose']['name']
        #shutil.copy(self.waitingReadUserChoose, resDic['source']['path'])
        """
        for value in [ waitingReadXlsxDic.get(value) for value in list(waitingReadXlsxDic.keys()) ]:

            #Search the Key source file
            if not self.search_fileOrdir(value['name'],resDic['source']['path']) \
               and not os.path.isfile(value['name']):
                print("All Not found: %s"%value['name'])
                value['isExist'] = False
                if ([ False ]*len(list(waitingReadXlsxDic.keys)) == \
				[ waitingReadXlsxDic.get(value)['isExist'] for value in list(waitingReadXlsxDic.keys()) ]):
                    print("Exiting ...")
                    return
                continue

            elif not self.search_fileOrdir(value['name'],resDic['source']['path']):
                shutil.copy(value['name'], resDic['source']['path'])
                print("%s Exist ,Copy to %s"%(resDic['local']['path'],resDic['source']['path']))

            elif not os.path.isfile(value['name']):
                shutil.copy(resDic['source']['path'] + value['name'], resDic['local']['path'])
                print("%s Exist ,Copy to %s"%(resDic['source']['path'],resDic['local']['path']))

        if waitingReadXlsxDic['waitingReadRealTimeXlsx']['isExist']:
            waitingReadXlsx = waitingReadXlsxDic['waitingReadRealTimeXlsx']['name']
        else:
            waitingReadXlsx = waitingReadXlsxDic['waitingReadBacXlsx']['name']

		"""

        #key source file
        resDic['source']['waitingReadXlsx'] = self.waitingReadUserChoose
        #resDic['source']['waitingReadXlsx'] = resDic['source']['path'] + waitingReadXlsx

        #Fill up the temp file pickle to backup data
        resDic['temp']['pickle'] = [ {'name': resDic['temp']['path'] + value[0],'item': value[1] } for value in list(zip(list_pickle, mainItems))]

        #generate file

        resDic['generate']['xlsx_0'] = resDic['generate']['path'] + saved_XlsxName
        resDic['generate']['text'] = [ resDic['generate']['path'] + value for value in saved_textName ]
        #print(resDic['generate']['xlsx_0'],resDic['generate']['text'])

        self.saved_XlsxName = saved_XlsxName
        self.resDic = resDic

        return resDic

    def amazon_progree(self,index,length,num):
        try:
            self.mQueue.put({'index':index,'length':length,'num':num},block = False)
        except:
            print('print error')


    def amazon_print(self, msg):
        v = type(msg)
        try:
            self.mQueue.put(str(msg),block = False)
        except:
            print('print error')
            pass

        for case in switch(v):
            if case(int):
                self._trigger_int.emit(msg)
                break
            if case(str):
                self._trigger_str.emit(msg)
                break
            if case(list):
                self._trigger_list.emit(msg)
                break
            if case(dict):
                self._trigger_dict.emit(msg)
                break
            if case():
                return





"""  
if __name__ == '__main__':
    amazon_stock = amazon_stock()
"""
    



    


    
    










