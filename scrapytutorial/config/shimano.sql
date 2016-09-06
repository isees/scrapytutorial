/*
Navicat MySQL Data Transfer

Source Server         : local
Source Server Version : 50712
Source Host           : localhost:3306
Source Database       : scrapy

Target Server Type    : MYSQL
Target Server Version : 50712
File Encoding         : 65001

Date: 2016-09-06 20:30:33
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for shimano
-- ----------------------------
DROP TABLE IF EXISTS `shimano`;
CREATE TABLE `shimano` (
  `id` int(10) NOT NULL,
  `name` varchar(255) NOT NULL COMMENT '名称',
  `source` int(3) DEFAULT NULL COMMENT '来源',
  `fitting_class` varchar(50) DEFAULT NULL COMMENT '分类',
  `fitting_series` varchar(255) DEFAULT NULL COMMENT '系列',
  `fitting_model` varchar(255) DEFAULT NULL COMMENT '型号',
  `fitting_type` varchar(255) DEFAULT NULL COMMENT '配件类型',
  `image_origin` varchar(255) DEFAULT NULL COMMENT '原图地址',
  `image_standard` varchar(255) DEFAULT NULL COMMENT '图片标准地址',
  `features` varchar(255) DEFAULT NULL COMMENT '特点',
  `attributes` varchar(255) DEFAULT NULL COMMENT '属性',
  `status` int(3) DEFAULT NULL COMMENT '状态',
  `update_time` int(10) DEFAULT NULL COMMENT '更新时间',
  `create_time` int(10) DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
