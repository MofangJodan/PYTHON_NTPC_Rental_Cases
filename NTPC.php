<?php
/* 
 新北市政府資料開放平臺
 資料集名稱	不動產實價登錄資訊-租賃案件
 資料集主題分類	地政
 國發會主題分類	購屋及遷徙
 主要欄位說明	district(鄉鎮市區)、rps01(交易標的)、rps02(土地區段位置建物區段門牌)、rps03(土地面積平方公尺)、rps04(都市土地使用分區)、rps05(非都市土地使用分區)、rps06(非都市土地使用編定)、rps07(租賃年月日)、rps08(租賃筆棟數)、rps09(租賃層次)、rps10(總樓層數)、rps11(建物型態)、rps12(主要用途)、rps13(主要建材)、rps14(建築完成年月)、rps15(建物總面積平方公尺)、rps16(建物現況格局-房)、rps17(建物現況格局-廳)、rps18(建物現況格局-衛)、rps19(建物現況格局-隔間)、rps20(有無管理組織)、rps21(有無附傢俱)、rps22(總額元)、rps23(單價元平方公尺)、rps24(車位類別)、rps25(車位面積平方公尺)、rps26(車位總額元)、rps27(備註)
*/

$source_url="https://data.ntpc.gov.tw//api/datasets/";
$source_key="71A2CA56-9F6B-45B6-ABE8-2B864A2C66DD";
$source_json="/json?page=";
$page_A="1";

for($page_A;$page_A<181;$page_A++)
{
	$AA = $source_url.$source_key.$source_json.$page_A;
	$json0_AA = file_get_contents($AA);
	$json0_AA1= json_decode($json0_AA);
	$zz=0;
	for($zz;$zz<30;$zz++)
		{
			$district=$json0_AA1[$zz]->district;
			$rps01=$json0_AA1[$zz]->rps01;
			$rps02=$json0_AA1[$zz]->rps02;
			$rps03=$json0_AA1[$zz]->rps03;
			$rps04=$json0_AA1[$zz]->rps04;
			$rps05=$json0_AA1[$zz]->rps05;
			$rps06=$json0_AA1[$zz]->rps06;
			$rps07=$json0_AA1[$zz]->rps07;
			$rps08=$json0_AA1[$zz]->rps08;
			$rps09=$json0_AA1[$zz]->rps09;
			$rps10=$json0_AA1[$zz]->rps10;
			$rps11=$json0_AA1[$zz]->rps11;
			$rps12=$json0_AA1[$zz]->rps12;
			$rps13=$json0_AA1[$zz]->rps13;
			$rps14=$json0_AA1[$zz]->rps14;
			$rps15=$json0_AA1[$zz]->rps15;
			$rps16=$json0_AA1[$zz]->rps16;
			$rps17=$json0_AA1[$zz]->rps17;
			$rps18=$json0_AA1[$zz]->rps18;
			$rps19=$json0_AA1[$zz]->rps19;
			$rps20=$json0_AA1[$zz]->rps20;
			$rps21=$json0_AA1[$zz]->rps21;
			$rps22=$json0_AA1[$zz]->rps22;
			$rps23=$json0_AA1[$zz]->rps23;
			$rps24=$json0_AA1[$zz]->rps24;
			$rps25=$json0_AA1[$zz]->rps25;
			$rps26=$json0_AA1[$zz]->rps26;
			$rps27=$json0_AA1[$zz]->rps27;

			$server = '127.0.0.1'; //資料庫位置
			$dbuser = 'root'; //資料庫帳號
			$dbpassword = ''; //資料庫密碼
			$dbname = 'ntpc'; //資料庫
			$link = mysqli_connect($server,$dbuser,$dbpassword,$dbname,3306);
			if(!$link){
				echo "資料庫連接失敗";
				exit();
			}
			else{
			mysqli_query( $link, "SET NAMES 'utf8'");

			$sql_log="INSERT INTO Rental_Cases 
			(district,rps01,rps02,rps03,rps04,rps05,rps06,rps07,rps08,rps09,rps10,rps11,rps12,rps13,rps14,rps15,rps16,rps17,rps18,rps19,rps20,rps21,rps22,rps23,rps24,rps25,rps26,rps27)
			value ('$district','$rps01','$rps02','$rps03','$rps04','$rps05','$rps06','$rps07','$rps08','$rps09','$rps10','$rps11','$rps12','$rps13','$rps14','$rps15','$rps16','$rps17','$rps18','$rps19','$rps20','$rps21','$rps22','$rps23','$rps24','$rps25','$rps26','$rps27')";
				if ($link->query($sql_log) === TRUE) {
					echo "新增資料";
				} else {
					echo "資料更新失敗: " . $link->error;
						}
				}
		}
}
?>