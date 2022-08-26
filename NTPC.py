# 新北市政府資料開放平臺
# 資料集名稱	不動產實價登錄資訊-租賃案件
# 資料集主題分類	地政
# 國發會主題分類	購屋及遷徙
# 主要欄位說明	district(鄉鎮市區)、rps01(交易標的)、rps02(土地區段位置建物區段門牌)、rps03(土地面積平方公尺)、rps04(都市土地使用分區)、rps05(非都市土地使用分區)、rps06(非都市土地使用編定)、rps07(租賃年月日)、rps08(租賃筆棟數)、rps09(租賃層次)、rps10(總樓層數)、rps11(建物型態)、rps12(主要用途)、rps13(主要建材)、rps14(建築完成年月)、rps15(建物總面積平方公尺)、rps16(建物現況格局-房)、rps17(建物現況格局-廳)、rps18(建物現況格局-衛)、rps19(建物現況格局-隔間)、rps20(有無管理組織)、rps21(有無附傢俱)、rps22(總額元)、rps23(單價元平方公尺)、rps24(車位類別)、rps25(車位面積平方公尺)、rps26(車位總額元)、rps27(備註)

import json, requests 
import pymysql

source_url="https://data.ntpc.gov.tw//api/datasets/" # 新北市政府資料開放平臺
source_url1="71A2CA56-9F6B-45B6-ABE8-2B864A2C66DD" # 不動產實價登錄資訊-租賃案件
source_url0="/json?page=" # 不動產實價登錄資訊-租賃案件 頁面
SS1 = source_url+source_url1
SS2=SS1+source_url0
for pages in range(0,188):
    SS=SS2+str(pages)
    url = requests.get(SS)
    text = url.json()
    for c in range(0,29):
        temp_district=text[c]['district'] #鄉鎮市區     
        temp_rps01=text[c]['rps01'] #交易標的
        temp_rps02=text[c]['rps02'] #土地區段位置建物區段門牌        
        temp_rps03=text[c]['rps03'] #土地面積平方公尺        
        temp_rps04=text[c]['rps04'] #都市土地使用分區        
        temp_rps05=text[c]['rps05'] #非都市土地使用分區        
        temp_rps06=text[c]['rps06'] #非都市土地使用編定        
        temp_rps07=text[c]['rps07'] #租賃年月日        
        temp_rps08=text[c]['rps08'] #租賃筆棟數        
        temp_rps09=text[c]['rps09'] #租賃層次        
        temp_rps10=text[c]['rps10'] #總樓層數        
        temp_rps11=text[c]['rps11'] #建物型態        
        temp_rps12=text[c]['rps12'] #主要用途        
        temp_rps13=text[c]['rps13'] #主要建材        
        temp_rps14=text[c]['rps14'] #建築完成年月        
        temp_rps15=text[c]['rps15'] #建物總面積平方公尺        
        temp_rps16=text[c]['rps16'] #建物現況格局        
        temp_rps17=text[c]['rps17'] #建物現況格局-廳        
        temp_rps18=text[c]['rps18'] #建物現況格局-衛        
        temp_rps19=text[c]['rps19'] #建物現況格局-隔間        
        temp_rps20=text[c]['rps20'] #有無管理組織        
        temp_rps21=text[c]['rps21'] #有無附傢俱        
        temp_rps22=text[c]['rps22'] #總額元        
        temp_rps23=text[c]['rps23'] #單價元平方公尺        
        temp_rps24=text[c]['rps24'] #車位類別        
        temp_rps25=text[c]['rps25'] #車位面積平方公尺        
        temp_rps26=text[c]['rps26'] #車位總額元
        temp_rps27=text[c]['rps27'] #備註

        d = {
        "Atemp_district":temp_district,
        "Atemp_rps01":temp_rps01,
        "Atemp_rps02":temp_rps02,
        "Atemp_rps03":temp_rps03,
        "Atemp_rps04":temp_rps04,
        "Atemp_rps05":temp_rps05,
        "Atemp_rps06":temp_rps06,
        "Atemp_rps07":temp_rps07,
        "Atemp_rps08":temp_rps08,
        "Atemp_rps09":temp_rps09,
        "Atemp_rps10":temp_rps10,
        "Atemp_rps11":temp_rps11,
        "Atemp_rps12":temp_rps12,
        "Atemp_rps13":temp_rps13,
        "Atemp_rps14":temp_rps14,
        "Atemp_rps15":temp_rps15,
        "Atemp_rps16":temp_rps16,
        "Atemp_rps17":temp_rps17,
        "Atemp_rps18":temp_rps18,
        "Atemp_rps19":temp_rps19,
        "Atemp_rps20":temp_rps20,
        "Atemp_rps21":temp_rps21,
        "Atemp_rps22":temp_rps22,
        "Atemp_rps23":temp_rps23,
        "Atemp_rps24":temp_rps24,
        "Atemp_rps25":temp_rps25,
        "Atemp_rps26":temp_rps26,
        "Atemp_rps27":temp_rps27
        }
        db = pymysql.connect(host='127.0.0.1',user='root',password='',db='ntpc')
        cursor = db.cursor()
        sql="INSERT INTO Rental_Cases (district,rps01,rps02,rps03,rps04,rps05,rps06,rps07,rps08,rps09,rps10,rps11,rps12,rps13,rps14,rps15,rps16,rps17,rps18,rps19,rps20,rps21,rps22,rps23,rps24,rps25,rps26,rps27) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}','{14}','{15}','{16}','{17}','{18}','{19}','{20}','{21}','{22}','{23}','{24}','{25}','{26}','{27}')"
        sql = sql.format(d['Atemp_district'],d['Atemp_rps01'],d['Atemp_rps02'],d['Atemp_rps03'],d['Atemp_rps04'],d['Atemp_rps05'],d['Atemp_rps06'],d['Atemp_rps07'],d['Atemp_rps08'],d['Atemp_rps09'],d['Atemp_rps10'],d['Atemp_rps11'],d['Atemp_rps12'],d['Atemp_rps13'],d['Atemp_rps14'],d['Atemp_rps15'],d['Atemp_rps16'],d['Atemp_rps17'],d['Atemp_rps18'],d['Atemp_rps19'],d['Atemp_rps20'],d['Atemp_rps21'],d['Atemp_rps22'],d['Atemp_rps23'],d['Atemp_rps24'],d['Atemp_rps25'],d['Atemp_rps26'],d['Atemp_rps27'])

        try:
            cursor.execute(sql)
            db.commit()
            print("新增資料成功")
        except:
            db.rollback()
            print("新增失敗")
        db.close()
