/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50722
Source Host           : localhost:3306
Source Database       : baicao

Target Server Type    : MYSQL
Target Server Version : 50722
File Encoding         : 65001

Date: 2018-07-24 21:07:40
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can view log entry', '1', 'view_logentry');
INSERT INTO `auth_permission` VALUES ('5', 'Can add group', '2', 'add_group');
INSERT INTO `auth_permission` VALUES ('6', 'Can change group', '2', 'change_group');
INSERT INTO `auth_permission` VALUES ('7', 'Can delete group', '2', 'delete_group');
INSERT INTO `auth_permission` VALUES ('8', 'Can add permission', '3', 'add_permission');
INSERT INTO `auth_permission` VALUES ('9', 'Can change permission', '3', 'change_permission');
INSERT INTO `auth_permission` VALUES ('10', 'Can delete permission', '3', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('11', 'Can view group', '2', 'view_group');
INSERT INTO `auth_permission` VALUES ('12', 'Can view permission', '3', 'view_permission');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '4', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '4', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '4', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can view content type', '4', 'view_contenttype');
INSERT INTO `auth_permission` VALUES ('17', 'Can add session', '5', 'add_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can change session', '5', 'change_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can delete session', '5', 'delete_session');
INSERT INTO `auth_permission` VALUES ('20', 'Can view session', '5', 'view_session');
INSERT INTO `auth_permission` VALUES ('21', 'Can add 新闻信息', '6', 'add_news');
INSERT INTO `auth_permission` VALUES ('22', 'Can change 新闻信息', '6', 'change_news');
INSERT INTO `auth_permission` VALUES ('23', 'Can delete 新闻信息', '6', 'delete_news');
INSERT INTO `auth_permission` VALUES ('24', 'Can add 基地信息', '7', 'add_base');
INSERT INTO `auth_permission` VALUES ('25', 'Can change 基地信息', '7', 'change_base');
INSERT INTO `auth_permission` VALUES ('26', 'Can delete 基地信息', '7', 'delete_base');
INSERT INTO `auth_permission` VALUES ('27', 'Can add 员工信息', '8', 'add_staff');
INSERT INTO `auth_permission` VALUES ('28', 'Can change 员工信息', '8', 'change_staff');
INSERT INTO `auth_permission` VALUES ('29', 'Can delete 员工信息', '8', 'delete_staff');
INSERT INTO `auth_permission` VALUES ('30', 'Can add 用户信息', '9', 'add_userprofile');
INSERT INTO `auth_permission` VALUES ('31', 'Can change 用户信息', '9', 'change_userprofile');
INSERT INTO `auth_permission` VALUES ('32', 'Can delete 用户信息', '9', 'delete_userprofile');
INSERT INTO `auth_permission` VALUES ('33', 'Can add 轮播图', '10', 'add_banner');
INSERT INTO `auth_permission` VALUES ('34', 'Can change 轮播图', '10', 'change_banner');
INSERT INTO `auth_permission` VALUES ('35', 'Can delete 轮播图', '10', 'delete_banner');
INSERT INTO `auth_permission` VALUES ('36', 'Can view 轮播图', '10', 'view_banner');
INSERT INTO `auth_permission` VALUES ('37', 'Can view 基地信息', '7', 'view_base');
INSERT INTO `auth_permission` VALUES ('38', 'Can view 新闻信息', '6', 'view_news');
INSERT INTO `auth_permission` VALUES ('39', 'Can view 员工信息', '8', 'view_staff');
INSERT INTO `auth_permission` VALUES ('40', 'Can view 用户信息', '9', 'view_userprofile');
INSERT INTO `auth_permission` VALUES ('41', 'Can add 代种信息', '11', 'add_generation');
INSERT INTO `auth_permission` VALUES ('42', 'Can change 代种信息', '11', 'change_generation');
INSERT INTO `auth_permission` VALUES ('43', 'Can delete 代种信息', '11', 'delete_generation');
INSERT INTO `auth_permission` VALUES ('44', 'Can add 收藏信息', '12', 'add_favorite');
INSERT INTO `auth_permission` VALUES ('45', 'Can change 收藏信息', '12', 'change_favorite');
INSERT INTO `auth_permission` VALUES ('46', 'Can delete 收藏信息', '12', 'delete_favorite');
INSERT INTO `auth_permission` VALUES ('47', 'Can add 购买信息', '13', 'add_purchase');
INSERT INTO `auth_permission` VALUES ('48', 'Can change 购买信息', '13', 'change_purchase');
INSERT INTO `auth_permission` VALUES ('49', 'Can delete 购买信息', '13', 'delete_purchase');
INSERT INTO `auth_permission` VALUES ('50', 'Can view 收藏信息', '12', 'view_favorite');
INSERT INTO `auth_permission` VALUES ('51', 'Can view 代种信息', '11', 'view_generation');
INSERT INTO `auth_permission` VALUES ('52', 'Can view 购买信息', '13', 'view_purchase');
INSERT INTO `auth_permission` VALUES ('53', 'Can add 商品信息', '14', 'add_goods');
INSERT INTO `auth_permission` VALUES ('54', 'Can change 商品信息', '14', 'change_goods');
INSERT INTO `auth_permission` VALUES ('55', 'Can delete 商品信息', '14', 'delete_goods');
INSERT INTO `auth_permission` VALUES ('56', 'Can add 植物信息', '15', 'add_plants');
INSERT INTO `auth_permission` VALUES ('57', 'Can change 植物信息', '15', 'change_plants');
INSERT INTO `auth_permission` VALUES ('58', 'Can delete 植物信息', '15', 'delete_plants');
INSERT INTO `auth_permission` VALUES ('59', 'Can view 商品信息', '14', 'view_goods');
INSERT INTO `auth_permission` VALUES ('60', 'Can view 植物信息', '15', 'view_plants');
INSERT INTO `auth_permission` VALUES ('61', 'Can add log entry', '16', 'add_log');
INSERT INTO `auth_permission` VALUES ('62', 'Can change log entry', '16', 'change_log');
INSERT INTO `auth_permission` VALUES ('63', 'Can delete log entry', '16', 'delete_log');
INSERT INTO `auth_permission` VALUES ('64', 'Can add User Widget', '17', 'add_userwidget');
INSERT INTO `auth_permission` VALUES ('65', 'Can change User Widget', '17', 'change_userwidget');
INSERT INTO `auth_permission` VALUES ('66', 'Can delete User Widget', '17', 'delete_userwidget');
INSERT INTO `auth_permission` VALUES ('67', 'Can add Bookmark', '18', 'add_bookmark');
INSERT INTO `auth_permission` VALUES ('68', 'Can change Bookmark', '18', 'change_bookmark');
INSERT INTO `auth_permission` VALUES ('69', 'Can delete Bookmark', '18', 'delete_bookmark');
INSERT INTO `auth_permission` VALUES ('70', 'Can add User Setting', '19', 'add_usersettings');
INSERT INTO `auth_permission` VALUES ('71', 'Can change User Setting', '19', 'change_usersettings');
INSERT INTO `auth_permission` VALUES ('72', 'Can delete User Setting', '19', 'delete_usersettings');
INSERT INTO `auth_permission` VALUES ('73', 'Can view Bookmark', '18', 'view_bookmark');
INSERT INTO `auth_permission` VALUES ('74', 'Can view log entry', '16', 'view_log');
INSERT INTO `auth_permission` VALUES ('75', 'Can view User Setting', '19', 'view_usersettings');
INSERT INTO `auth_permission` VALUES ('76', 'Can view User Widget', '17', 'view_userwidget');

-- ----------------------------
-- Table structure for banner
-- ----------------------------
DROP TABLE IF EXISTS `banner`;
CREATE TABLE `banner` (
  `index` int(11) NOT NULL AUTO_INCREMENT,
  `add_time` datetime(6) NOT NULL,
  `content_id` int(11) NOT NULL,
  PRIMARY KEY (`index`),
  KEY `banner_content_id_9778c085_fk_users_news_id` (`content_id`),
  CONSTRAINT `banner_content_id_9778c085_fk_users_news_id` FOREIGN KEY (`content_id`) REFERENCES `users_news` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of banner
-- ----------------------------

-- ----------------------------
-- Table structure for base
-- ----------------------------
DROP TABLE IF EXISTS `base`;
CREATE TABLE `base` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of base
-- ----------------------------
INSERT INTO `base` VALUES ('1', '绪论', '南京市栖霞区仙林大道', '2018-07-14 00:00:00.000000');
INSERT INTO `base` VALUES ('2', '南京', '仙林大道138号', '2018-07-14 00:00:00.000000');

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('12', 'operation', 'favorite');
INSERT INTO `django_content_type` VALUES ('11', 'operation', 'generation');
INSERT INTO `django_content_type` VALUES ('13', 'operation', 'purchase');
INSERT INTO `django_content_type` VALUES ('14', 'product', 'goods');
INSERT INTO `django_content_type` VALUES ('15', 'product', 'plants');
INSERT INTO `django_content_type` VALUES ('5', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('10', 'users', 'banner');
INSERT INTO `django_content_type` VALUES ('7', 'users', 'base');
INSERT INTO `django_content_type` VALUES ('6', 'users', 'news');
INSERT INTO `django_content_type` VALUES ('8', 'users', 'staff');
INSERT INTO `django_content_type` VALUES ('9', 'users', 'userprofile');
INSERT INTO `django_content_type` VALUES ('18', 'xadmin', 'bookmark');
INSERT INTO `django_content_type` VALUES ('16', 'xadmin', 'log');
INSERT INTO `django_content_type` VALUES ('19', 'xadmin', 'usersettings');
INSERT INTO `django_content_type` VALUES ('17', 'xadmin', 'userwidget');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2018-07-13 08:22:20.321771');
INSERT INTO `django_migrations` VALUES ('2', 'contenttypes', '0002_remove_content_type_name', '2018-07-13 08:22:21.259437');
INSERT INTO `django_migrations` VALUES ('3', 'auth', '0001_initial', '2018-07-13 08:22:24.540867');
INSERT INTO `django_migrations` VALUES ('4', 'auth', '0002_alter_permission_name_max_length', '2018-07-13 08:22:25.150204');
INSERT INTO `django_migrations` VALUES ('5', 'auth', '0003_alter_user_email_max_length', '2018-07-13 08:22:25.181490');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0004_alter_user_username_opts', '2018-07-13 08:22:25.228508');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0005_alter_user_last_login_null', '2018-07-13 08:22:25.244125');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0006_require_contenttypes_0002', '2018-07-13 08:22:25.275381');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0007_alter_validators_add_error_messages', '2018-07-13 08:22:25.337885');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0008_alter_user_username_max_length', '2018-07-13 08:22:25.384729');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0009_alter_user_last_name_max_length', '2018-07-13 08:22:25.447226');
INSERT INTO `django_migrations` VALUES ('12', 'users', '0001_initial', '2018-07-13 08:22:32.901086');
INSERT INTO `django_migrations` VALUES ('13', 'admin', '0001_initial', '2018-07-13 08:22:34.573275');
INSERT INTO `django_migrations` VALUES ('14', 'admin', '0002_logentry_remove_auto_add', '2018-07-13 08:22:34.620120');
INSERT INTO `django_migrations` VALUES ('15', 'product', '0001_initial', '2018-07-13 08:22:35.213951');
INSERT INTO `django_migrations` VALUES ('16', 'operation', '0001_initial', '2018-07-13 08:22:36.042046');
INSERT INTO `django_migrations` VALUES ('17', 'operation', '0002_auto_20180713_1621', '2018-07-13 08:22:43.793237');
INSERT INTO `django_migrations` VALUES ('18', 'product', '0002_goods_base', '2018-07-13 08:22:45.043280');
INSERT INTO `django_migrations` VALUES ('19', 'sessions', '0001_initial', '2018-07-13 08:22:45.497249');
INSERT INTO `django_migrations` VALUES ('20', 'xadmin', '0001_initial', '2018-07-13 08:22:49.263531');
INSERT INTO `django_migrations` VALUES ('21', 'xadmin', '0002_log', '2018-07-13 08:22:51.169787');
INSERT INTO `django_migrations` VALUES ('22', 'xadmin', '0003_auto_20160715_0100', '2018-07-13 08:22:52.185493');
INSERT INTO `django_migrations` VALUES ('23', 'operation', '0003_auto_20180713_1739', '2018-07-13 09:39:59.795778');
INSERT INTO `django_migrations` VALUES ('24', 'users', '0002_auto_20180714_0911', '2018-07-14 01:12:16.120173');
INSERT INTO `django_migrations` VALUES ('25', 'operation', '0004_auto_20180723_1141', '2018-07-23 03:41:29.755753');
INSERT INTO `django_migrations` VALUES ('26', 'product', '0003_auto_20180723_1141', '2018-07-23 03:41:29.818700');
INSERT INTO `django_migrations` VALUES ('27', 'users', '0003_auto_20180723_1141', '2018-07-23 03:41:31.924450');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('p0cfetwwm1fwkozt87q28rdbs3bh0431', 'Y2Y2ZDI3YzgyNzg5YTAxOTNmNjk3NDQyNmU1Yjk4Y2Y5YzAxZjllYTp7IkxJU1RfUVVFUlkiOltbInByb2R1Y3QiLCJnb29kcyJdLCIiXSwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfaGFzaCI6ImNmZmQwNTYwMDRmZGQwNGNjNmFiZTA1OTllZjYzNDNmYmI4ZDRmYzIifQ==', '2018-07-28 01:37:49.151395');
INSERT INTO `django_session` VALUES ('qhtaw1y27qsgr7ld0xjrgoi20ay439t4', 'NGFjYjhiNTVhZDU5Njg0Y2NjOWY0ZDAxOWYzN2FiNWIzMGY2NWEwNDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiY2ZmZDA1NjAwNGZkZDA0Y2M2YWJlMDU5OWVmNjM0M2ZiYjhkNGZjMiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiTElTVF9RVUVSWSI6W1sib3BlcmF0aW9uIiwiZ2VuZXJhdGlvbiJdLCIiXX0=', '2018-07-27 23:46:04.803236');
INSERT INTO `django_session` VALUES ('y6eb0y47xpttypwt8sy7f5tvigvu4ew3', 'ZTkzNGZlMGI3NGQ0MDk2MTBjODAwZjk1N2Q4YWM4ZTM1ODI5NzU4Yjp7IkxJU1RfUVVFUlkiOltbInVzZXJzIiwic3RhZmYiXSwiIl0sIl9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiY2ZmZDA1NjAwNGZkZDA0Y2M2YWJlMDU5OWVmNjM0M2ZiYjhkNGZjMiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2018-07-28 05:09:34.313204');

-- ----------------------------
-- Table structure for favorite
-- ----------------------------
DROP TABLE IF EXISTS `favorite`;
CREATE TABLE `favorite` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `add_time` datetime(6) NOT NULL,
  `good_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `favorite_good_id_4f8ed2e4_fk_goods_id` (`good_id`),
  KEY `favorite_user_id_8a5f8d2c_fk_user_id` (`user_id`),
  CONSTRAINT `favorite_good_id_4f8ed2e4_fk_goods_id` FOREIGN KEY (`good_id`) REFERENCES `goods` (`id`),
  CONSTRAINT `favorite_user_id_8a5f8d2c_fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of favorite
-- ----------------------------

-- ----------------------------
-- Table structure for generation
-- ----------------------------
DROP TABLE IF EXISTS `generation`;
CREATE TABLE `generation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `begin` date NOT NULL,
  `end` date NOT NULL,
  `deliver_type` varchar(10) NOT NULL,
  `plant_type` varchar(10) NOT NULL,
  `address` varchar(50) NOT NULL,
  `price` double NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `staff_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `generation_customer_id_53dec98d_fk_user_id` (`customer_id`),
  KEY `generation_staff_id_9c30f852_fk_staff_id` (`staff_id`),
  CONSTRAINT `generation_customer_id_53dec98d_fk_user_id` FOREIGN KEY (`customer_id`) REFERENCES `user` (`id`),
  CONSTRAINT `generation_staff_id_9c30f852_fk_staff_id` FOREIGN KEY (`staff_id`) REFERENCES `staff` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of generation
-- ----------------------------

-- ----------------------------
-- Table structure for goods
-- ----------------------------
DROP TABLE IF EXISTS `goods`;
CREATE TABLE `goods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `type` varchar(10) NOT NULL,
  `price` double NOT NULL,
  `count` int(11) NOT NULL,
  `desc` varchar(200) NOT NULL,
  `img` varchar(100) NOT NULL,
  `add_time` date NOT NULL,
  `base_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `goods_base_id_de5ed996_fk_base_id` (`base_id`),
  CONSTRAINT `goods_base_id_de5ed996_fk_base_id` FOREIGN KEY (`base_id`) REFERENCES `base` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of goods
-- ----------------------------
INSERT INTO `goods` VALUES ('1', 'test', 'seed', '13', '1', 'test', 'image/goods/2018/07/001.jpg', '2018-07-14', '1');

-- ----------------------------
-- Table structure for plants
-- ----------------------------
DROP TABLE IF EXISTS `plants`;
CREATE TABLE `plants` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `classes` varchar(50) NOT NULL,
  `specification` varchar(50) NOT NULL,
  `phase` varchar(50) NOT NULL,
  `parts` varchar(50) NOT NULL,
  `flavour` varchar(50) NOT NULL,
  `function` varchar(50) NOT NULL,
  `image` varchar(100) NOT NULL,
  `add_time` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of plants
-- ----------------------------
INSERT INTO `plants` VALUES ('1', '吉林', '个人', '片', 'test', 'test', 'test', 'test', 'image/plants/2018/07/011618576a5a5c0000018c1bea80fe.jpg1280w_1l_2o_100sh.jpg', '2018-07-14');

-- ----------------------------
-- Table structure for purchase
-- ----------------------------
DROP TABLE IF EXISTS `purchase`;
CREATE TABLE `purchase` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `count` int(11) NOT NULL,
  `total_money` double NOT NULL,
  `state` int(11) NOT NULL,
  `address` varchar(50) NOT NULL,
  `mobile_phone` varchar(11) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `goods_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `purchase_goods_id_aa628f17_fk_goods_id` (`goods_id`),
  KEY `purchase_customer_id_332935c6_fk_user_id` (`customer_id`),
  CONSTRAINT `purchase_customer_id_332935c6_fk_user_id` FOREIGN KEY (`customer_id`) REFERENCES `user` (`id`),
  CONSTRAINT `purchase_goods_id_aa628f17_fk_goods_id` FOREIGN KEY (`goods_id`) REFERENCES `goods` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of purchase
-- ----------------------------
INSERT INTO `purchase` VALUES ('1', '1', '111', '1', '111', '15105185056', '2018-07-23 00:00:00.000000', '1', '1');
INSERT INTO `purchase` VALUES ('2', '1', '111', '1', '111', '15105185056', '2018-07-23 03:41:46.010105', '1', '1');
INSERT INTO `purchase` VALUES ('3', '1', '111', '1', '111', '15105185056', '2018-07-23 03:42:36.073727', '1', '1');
INSERT INTO `purchase` VALUES ('4', '1', '111', '1', '111', '15105185056', '2018-07-23 11:44:37.236392', '1', '1');

-- ----------------------------
-- Table structure for staff
-- ----------------------------
DROP TABLE IF EXISTS `staff`;
CREATE TABLE `staff` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `mobile_phone` varchar(12) NOT NULL,
  `salary` double NOT NULL,
  `seniority` int(11) DEFAULT NULL,
  `add_time` date NOT NULL,
  `base_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `staff_base_id_c90e8aff_fk_base_id` (`base_id`),
  CONSTRAINT `staff_base_id_c90e8aff_fk_base_id` FOREIGN KEY (`base_id`) REFERENCES `base` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of staff
-- ----------------------------
INSERT INTO `staff` VALUES ('1', '唐德才', '123456', '5000', '12', '2018-07-14', '1');
INSERT INTO `staff` VALUES ('2', 'cy', '123456', '7800', '14', '2018-07-14', '2');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `nick_name` varchar(50) NOT NULL,
  `gender` varchar(2) DEFAULT NULL,
  `mobile_phone` varchar(12) NOT NULL,
  `address` varchar(50) NOT NULL,
  `email` varchar(254) DEFAULT NULL,
  `image` varchar(100) NOT NULL,
  `wallet` double NOT NULL,
  `add_time` date NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `mobile_phone` (`mobile_phone`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', 'pbkdf2_sha256$100000$A3g4jfRiIcTm$DsVmB9Jy2kSaB4fYsAK1iRndkr8BTRBrd5bY06UHM/c=', '2018-07-13 09:35:28.333699', '1', 'test', '', '', '1', '1', '2018-07-13 08:25:02.404576', '', null, '', '', '1028813178@qq.com', '', '100', '2018-07-13');

-- ----------------------------
-- Table structure for users_news
-- ----------------------------
DROP TABLE IF EXISTS `users_news`;
CREATE TABLE `users_news` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `image` varchar(100) NOT NULL,
  `title` varchar(1024) NOT NULL,
  `content` varchar(2048) NOT NULL,
  `author` varchar(20) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users_news
-- ----------------------------
INSERT INTO `users_news` VALUES ('1', 'image/news/2018/07/001.jpg', 'test', 'test-demo', 'test', '2018-07-14 00:00:00.000000');

-- ----------------------------
-- Table structure for user_groups
-- ----------------------------
DROP TABLE IF EXISTS `user_groups`;
CREATE TABLE `user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_groups_userprofile_id_group_id_4f89dcbd_uniq` (`userprofile_id`,`group_id`),
  KEY `user_groups_group_id_b76f8aba_fk_auth_group_id` (`group_id`),
  CONSTRAINT `user_groups_group_id_b76f8aba_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_groups_userprofile_id_beb76c2d_fk_user_id` FOREIGN KEY (`userprofile_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `user_user_permissions`;
CREATE TABLE `user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_user_permissions_userprofile_id_permission_id_4ee72930_uniq` (`userprofile_id`,`permission_id`),
  KEY `user_user_permission_permission_id_9deb68a3_fk_auth_perm` (`permission_id`),
  CONSTRAINT `user_user_permission_permission_id_9deb68a3_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_user_permissions_userprofile_id_e8e85966_fk_user_id` FOREIGN KEY (`userprofile_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for xadmin_bookmark
-- ----------------------------
DROP TABLE IF EXISTS `xadmin_bookmark`;
CREATE TABLE `xadmin_bookmark` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(128) NOT NULL,
  `url_name` varchar(64) NOT NULL,
  `query` varchar(1000) NOT NULL,
  `is_share` tinyint(1) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_bookmark_content_type_id_60941679_fk_django_co` (`content_type_id`),
  KEY `xadmin_bookmark_user_id_42d307fc_fk_user_id` (`user_id`),
  CONSTRAINT `xadmin_bookmark_content_type_id_60941679_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `xadmin_bookmark_user_id_42d307fc_fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of xadmin_bookmark
-- ----------------------------

-- ----------------------------
-- Table structure for xadmin_log
-- ----------------------------
DROP TABLE IF EXISTS `xadmin_log`;
CREATE TABLE `xadmin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `ip_addr` char(39) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` varchar(32) NOT NULL,
  `message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_log_content_type_id_2a6cb852_fk_django_content_type_id` (`content_type_id`),
  KEY `xadmin_log_user_id_bb16a176_fk_user_id` (`user_id`),
  CONSTRAINT `xadmin_log_content_type_id_2a6cb852_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `xadmin_log_user_id_bb16a176_fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of xadmin_log
-- ----------------------------
INSERT INTO `xadmin_log` VALUES ('1', '2018-07-14 01:13:20.772926', '127.0.0.1', '1', 'test written By test', 'create', '已添加。', '6', '1');
INSERT INTO `xadmin_log` VALUES ('2', '2018-07-14 01:14:32.347282', '127.0.0.1', '1', '绪论', 'create', '已添加。', '7', '1');
INSERT INTO `xadmin_log` VALUES ('3', '2018-07-14 01:37:49.048278', '127.0.0.1', '1', 'test', 'create', '已添加。', '14', '1');
INSERT INTO `xadmin_log` VALUES ('4', '2018-07-14 03:44:08.884484', '127.0.0.1', '1', '吉林', 'create', '已添加。', '15', '1');
INSERT INTO `xadmin_log` VALUES ('5', '2018-07-14 05:08:21.385924', '127.0.0.1', '1', '唐德才', 'create', '已添加。', '8', '1');
INSERT INTO `xadmin_log` VALUES ('6', '2018-07-14 05:08:41.899698', '127.0.0.1', '2', '南京', 'create', '已添加。', '7', '1');
INSERT INTO `xadmin_log` VALUES ('7', '2018-07-14 05:09:02.551283', '127.0.0.1', '2', 'cy', 'create', '已添加。', '8', '1');

-- ----------------------------
-- Table structure for xadmin_usersettings
-- ----------------------------
DROP TABLE IF EXISTS `xadmin_usersettings`;
CREATE TABLE `xadmin_usersettings` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `key` varchar(256) NOT NULL,
  `value` longtext NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_usersettings_user_id_edeabe4a_fk_user_id` (`user_id`),
  CONSTRAINT `xadmin_usersettings_user_id_edeabe4a_fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of xadmin_usersettings
-- ----------------------------
INSERT INTO `xadmin_usersettings` VALUES ('1', 'dashboard:home:pos', '', '1');

-- ----------------------------
-- Table structure for xadmin_userwidget
-- ----------------------------
DROP TABLE IF EXISTS `xadmin_userwidget`;
CREATE TABLE `xadmin_userwidget` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `page_id` varchar(256) NOT NULL,
  `widget_type` varchar(50) NOT NULL,
  `value` longtext NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_userwidget_user_id_c159233a_fk_user_id` (`user_id`),
  CONSTRAINT `xadmin_userwidget_user_id_c159233a_fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of xadmin_userwidget
-- ----------------------------
