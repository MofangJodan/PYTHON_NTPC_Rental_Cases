-- 伺服器版本： 10.4.24-MariaDB
-- PHP 版本： 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `ntpc`
--

-- --------------------------------------------------------

--
-- 資料表結構 `rental_cases`
--

CREATE TABLE `rental_cases` (
  `id` int(11) NOT NULL COMMENT '編號',
  `district` text NOT NULL COMMENT '鄉鎮市區',
  `rps01` text DEFAULT NULL COMMENT '交易標的',
  `rps02` text DEFAULT NULL COMMENT '土地區段位置建物區段門牌',
  `rps03` text DEFAULT NULL COMMENT '土地面積平方公尺',
  `rps04` text DEFAULT NULL COMMENT '都市土地使用分區',
  `rps05` text DEFAULT NULL COMMENT '非都市土地使用分區',
  `rps06` text DEFAULT NULL COMMENT '非都市土地使用編定',
  `rps07` text DEFAULT NULL COMMENT '租賃年月日',
  `rps08` text DEFAULT NULL COMMENT '租賃筆棟數',
  `rps09` text DEFAULT NULL COMMENT '租賃層次',
  `rps10` text DEFAULT NULL COMMENT '總樓層數',
  `rps11` text DEFAULT NULL COMMENT '建物型態',
  `rps12` text DEFAULT NULL COMMENT '主要用途',
  `rps13` text DEFAULT NULL COMMENT '主要建材',
  `rps14` text DEFAULT NULL COMMENT '建築完成年月',
  `rps15` text DEFAULT NULL COMMENT '建物總面積平方公尺',
  `rps16` text DEFAULT NULL COMMENT '建物現況格局-房',
  `rps17` text DEFAULT NULL COMMENT '建物現況格局-廳',
  `rps18` text DEFAULT NULL COMMENT '建物現況格局-衛',
  `rps19` text DEFAULT NULL COMMENT '建物現況格局-隔間',
  `rps20` text DEFAULT NULL COMMENT '有無管理組織',
  `rps21` text DEFAULT NULL COMMENT '有無附傢俱',
  `rps22` text DEFAULT NULL COMMENT '總額元',
  `rps23` text DEFAULT NULL COMMENT '單價元平方公尺',
  `rps24` text DEFAULT NULL COMMENT '車位類別',
  `rps25` text DEFAULT NULL COMMENT '車位面積平方公尺',
  `rps26` text DEFAULT NULL COMMENT '車位總額元',
  `rps27` text DEFAULT NULL COMMENT '備註'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `rental_cases`
--
ALTER TABLE `rental_cases`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `rental_cases`
--
ALTER TABLE `rental_cases`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '編號';
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
