/*
 Navicat Premium Data Transfer

 Source Server         : local
 Source Server Type    : MySQL
 Source Server Version : 80026
 Source Host           : localhost:3306
 Source Schema         : wenjuan

 Target Server Type    : MySQL
 Target Server Version : 80026
 File Encoding         : 65001

 Date: 13/08/2021 08:58:03
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for tb_account
-- ----------------------------
DROP TABLE IF EXISTS `tb_account`;
CREATE TABLE `tb_account`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `nickname` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `openid` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `session_key` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_admin` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `avatar` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `finish_time` datetime NULL DEFAULT NULL,
  `regist_time` datetime NOT NULL,
  PRIMARY KEY (`id`, `openid`) USING BTREE,
  INDEX `openid`(`openid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 29 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of tb_account
-- ----------------------------

-- ----------------------------
-- Table structure for tb_baseinfo
-- ----------------------------
DROP TABLE IF EXISTS `tb_baseinfo`;
CREATE TABLE `tb_baseinfo`  (
  `openid` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `date` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `culture` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `erMing` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `during` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `keeping` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `env` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `voice` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `feel` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`openid`) USING BTREE,
  CONSTRAINT `baseInfo_account` FOREIGN KEY (`openid`) REFERENCES `tb_account` (`openid`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of tb_baseinfo
-- ----------------------------

-- ----------------------------
-- Table structure for tb_hist_disease
-- ----------------------------
DROP TABLE IF EXISTS `tb_hist_disease`;
CREATE TABLE `tb_hist_disease`  (
  `openid` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `symptom` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `reason` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `self_disease` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`openid`) USING BTREE,
  CONSTRAINT `tb_account_disease` FOREIGN KEY (`openid`) REFERENCES `tb_account` (`openid`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tb_hist_disease
-- ----------------------------

-- ----------------------------
-- Table structure for tb_option
-- ----------------------------
DROP TABLE IF EXISTS `tb_option`;
CREATE TABLE `tb_option`  (
  `id` int NOT NULL,
  `questionnaire_id` int NOT NULL,
  `content` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `option_questionnaire`(`questionnaire_id`) USING BTREE,
  CONSTRAINT `option_questionnaire` FOREIGN KEY (`questionnaire_id`) REFERENCES `tb_questionnaire` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of tb_option
-- ----------------------------
INSERT INTO `tb_option` VALUES (1, 1, '1. 耳鸣让你很难集中精力吗？');
INSERT INTO `tb_option` VALUES (2, 1, '2. 耳鸣的声音响度让你很难听清其他人说话吗？');
INSERT INTO `tb_option` VALUES (3, 1, '3. 耳鸣会让你生气吗？');
INSERT INTO `tb_option` VALUES (4, 1, '4. 耳鸣会让你困惑（烦恼）吗？');
INSERT INTO `tb_option` VALUES (5, 1, '5. 耳鸣使你有绝望的感觉吗？');
INSERT INTO `tb_option` VALUES (6, 1, '6.你总是抱怨耳鸣吗？');
INSERT INTO `tb_option` VALUES (7, 1, '7.耳鸣影响了你的睡眠吗？');
INSERT INTO `tb_option` VALUES (8, 1, '8.你是否觉得自己无法摆脱耳鸣？');
INSERT INTO `tb_option` VALUES (9, 1, '9.耳鸣干扰你的社交活动吗？（如出去吃晚餐，看电影）');
INSERT INTO `tb_option` VALUES (10, 1, '10.耳鸣使你沮丧吗？');
INSERT INTO `tb_option` VALUES (11, 1, '11.耳鸣是否让你觉得自己得了可怕的疾病吗？');
INSERT INTO `tb_option` VALUES (12, 1, '12.耳鸣让你很难享受生活吗？');
INSERT INTO `tb_option` VALUES (13, 1, '13.耳鸣干扰你的工作或家务吗？');
INSERT INTO `tb_option` VALUES (14, 1, '14.耳鸣让你容易发脾气吗？');
INSERT INTO `tb_option` VALUES (15, 1, '15.耳鸣会让你很难静下心做事吗？');
INSERT INTO `tb_option` VALUES (16, 1, '16.耳鸣让你心烦意乱吗？');
INSERT INTO `tb_option` VALUES (17, 1, '17.耳鸣使你和朋友或家人的关系紧张吗？');
INSERT INTO `tb_option` VALUES (18, 1, '18.注意力从耳鸣转移到其他事情有困难吗？');
INSERT INTO `tb_option` VALUES (19, 1, '19.你感到不能控制你的耳鸣吗？');
INSERT INTO `tb_option` VALUES (20, 1, '20.耳鸣会让你经常感到疲惫吗？');
INSERT INTO `tb_option` VALUES (21, 1, '21.耳鸣会让你情绪低落吗？做事情提不起兴趣？');
INSERT INTO `tb_option` VALUES (22, 1, '22.耳鸣会让你焦虑吗？');
INSERT INTO `tb_option` VALUES (23, 1, '23.你是否感到再也不能忍受耳鸣了？');
INSERT INTO `tb_option` VALUES (24, 1, '24.有压力时耳鸣会加重吗？');
INSERT INTO `tb_option` VALUES (25, 1, '25.耳鸣使你没有安全感吗？（不稳定，无保障）');
INSERT INTO `tb_option` VALUES (26, 2, '1.我觉得很难让自己安静下来');
INSERT INTO `tb_option` VALUES (27, 2, '2.我感到口干舌燥');
INSERT INTO `tb_option` VALUES (28, 2, '3.我好像一点都没有感觉到任何愉快、舒畅');
INSERT INTO `tb_option` VALUES (29, 2, '4.我感到呼吸困难（例如：气喘或透不过气来）');
INSERT INTO `tb_option` VALUES (30, 2, '5.我感到很难主动去开始工作');
INSERT INTO `tb_option` VALUES (31, 2, '6.我对事情往往做出过敏反应');
INSERT INTO `tb_option` VALUES (32, 2, '7.我感到颤抖（例如：手抖）');
INSERT INTO `tb_option` VALUES (33, 2, '8.我觉得自己消耗了很多精力');
INSERT INTO `tb_option` VALUES (34, 2, '9.我担心一些可能让自己恐慌或者出丑的场合');
INSERT INTO `tb_option` VALUES (35, 2, '10.我觉得自己对不久的将来没有什么可期盼的');
INSERT INTO `tb_option` VALUES (36, 2, '11.我感到忐忑不安');
INSERT INTO `tb_option` VALUES (37, 2, '12.我感到很难放松自己');
INSERT INTO `tb_option` VALUES (38, 2, '13.我感到悲伤沮丧');
INSERT INTO `tb_option` VALUES (39, 2, '14.我无法容忍任何阻碍我继续工作的事情');
INSERT INTO `tb_option` VALUES (40, 2, '15.我感到快要奔溃了');
INSERT INTO `tb_option` VALUES (41, 2, '16.我对任何事情都不能产生热情');
INSERT INTO `tb_option` VALUES (42, 2, '17.我觉得自己不怎么配做人');
INSERT INTO `tb_option` VALUES (43, 2, '18.我发现自己很容易被激怒');
INSERT INTO `tb_option` VALUES (44, 2, '19.即使在没有明显的体力活动时，我也感到心律不正常');
INSERT INTO `tb_option` VALUES (45, 2, '20.我无缘无故地感到害怕');
INSERT INTO `tb_option` VALUES (46, 2, '21.我感到生命毫无意义');
INSERT INTO `tb_option` VALUES (47, 3, '1.不表现出紧张对我来说很重要');
INSERT INTO `tb_option` VALUES (48, 3, '2.当我不能集中注意力在工作上时，我担心我可能会发疯');
INSERT INTO `tb_option` VALUES (49, 3, '3.心跳加快会使我害怕');
INSERT INTO `tb_option` VALUES (50, 3, '4.当我胃不适时，我担心自己可能病得很重');
INSERT INTO `tb_option` VALUES (51, 3, '5.不能集中注意力在工作上使我害怕');
INSERT INTO `tb_option` VALUES (52, 3, '6.在别人面前颤抖时，我担心别人对我的看法');
INSERT INTO `tb_option` VALUES (53, 3, '7.当我感到胸闷时，我害怕自己可能不能正常呼吸');
INSERT INTO `tb_option` VALUES (54, 3, '8.当我感到胸痛时，我担心我会心脏病发作');
INSERT INTO `tb_option` VALUES (55, 3, '9.我担心其他人可能会注意到我的焦虑');
INSERT INTO `tb_option` VALUES (56, 3, '10.当我感觉古怪或精神恍惚时，我担心自己可能得了心理疾病');
INSERT INTO `tb_option` VALUES (57, 3, '11.在他人面前脸红会使我害怕');
INSERT INTO `tb_option` VALUES (58, 3, '12.当我感觉自己心跳有一下停跳，我担心自己有非常严重的问题');
INSERT INTO `tb_option` VALUES (59, 3, '13.当我在社交场合流汗时，我会担心别人会对我有不好的看法');
INSERT INTO `tb_option` VALUES (60, 3, '14.当我思维加速时，我担心自己可能会发疯');
INSERT INTO `tb_option` VALUES (61, 3, '15.当我喉咙紧绷时，我担心自己出了问题');
INSERT INTO `tb_option` VALUES (62, 3, '16.当我不能清晰地思考问题时，我担心自己出了问题');
INSERT INTO `tb_option` VALUES (63, 3, '17.我认为在公共场合晕厥是令人恐惧的');
INSERT INTO `tb_option` VALUES (64, 3, '18.当我大脑空白时，我担心我出了严重的问题');
INSERT INTO `tb_option` VALUES (65, 4, '1.我常感到害怕');
INSERT INTO `tb_option` VALUES (66, 4, '2.一旦确定了目标，我会坚持努力地实现它');
INSERT INTO `tb_option` VALUES (67, 4, '3.我觉得大部分人基本上是心怀善意的');
INSERT INTO `tb_option` VALUES (68, 4, '4.我的头脑中经常充满生动的画面');
INSERT INTO `tb_option` VALUES (69, 4, '5.我对人多的聚会感到乏味');
INSERT INTO `tb_option` VALUES (70, 4, '6.有时我觉得自己一无是处');
INSERT INTO `tb_option` VALUES (71, 4, '7.我常常是仔细考虑后才做出决定');
INSERT INTO `tb_option` VALUES (72, 4, '8.我不太关心别人是否受到不公正的待遇');
INSERT INTO `tb_option` VALUES (73, 4, '9.我是一个勇于冒险，突破常规的人');
INSERT INTO `tb_option` VALUES (74, 4, '10.在热闹的聚会上，我常常表现主动并尽情玩耍');
INSERT INTO `tb_option` VALUES (75, 4, '11.别人一句漫不经心的话，我经常会联系在自己身上');
INSERT INTO `tb_option` VALUES (76, 4, '12.别人认为我是一个慎重的人');
INSERT INTO `tb_option` VALUES (77, 4, '13.我时常觉得别人的痛苦与我无关');
INSERT INTO `tb_option` VALUES (78, 4, '14.我喜欢冒险');
INSERT INTO `tb_option` VALUES (79, 4, '15.我尽量避免参加人多的聚会和处于嘈杂的环境');
INSERT INTO `tb_option` VALUES (80, 4, '16.在面对压力时，我有种快要奔溃的感觉');
INSERT INTO `tb_option` VALUES (81, 4, '17.我喜欢一开始就把事情计划好');
INSERT INTO `tb_option` VALUES (82, 4, '18.我是那种只照顾好自己，不替别人担忧的人');
INSERT INTO `tb_option` VALUES (83, 4, '19.我对许多事情有很强的好奇心');
INSERT INTO `tb_option` VALUES (84, 4, '20.有我在的场合一般不会冷场');
INSERT INTO `tb_option` VALUES (85, 4, '21.我常担心一些无关紧要的事');
INSERT INTO `tb_option` VALUES (86, 4, '22.我工作或学习很勤奋');
INSERT INTO `tb_option` VALUES (87, 4, '23.虽然社会上有骗子，但我相信大部分人还是可信的');
INSERT INTO `tb_option` VALUES (88, 4, '24.我身上具有别人没有的冒险精神');
INSERT INTO `tb_option` VALUES (89, 4, '25.在一个团体中，我希望处于领导地位');
INSERT INTO `tb_option` VALUES (90, 4, '26.我常常感到内心不踏实');
INSERT INTO `tb_option` VALUES (91, 4, '27.我是个倾尽全力做事的人');
INSERT INTO `tb_option` VALUES (92, 4, '28.当别人向我诉说不幸时，我常感到难过');
INSERT INTO `tb_option` VALUES (93, 4, '29.我渴望学习新东西，即使它们与我的日常生活无关');
INSERT INTO `tb_option` VALUES (94, 4, '30.别人大多认为我是一个热情和友好的人');
INSERT INTO `tb_option` VALUES (95, 4, '31.我常担心会有什么不好的事情要发生');
INSERT INTO `tb_option` VALUES (96, 4, '32.在工作上，我常只求能应付过去就好');
INSERT INTO `tb_option` VALUES (97, 4, '33.尽管人类社会存在一些阴暗的东西（如：战争、罪恶、欺诈），我仍然相信人性总的来说是善良的');
INSERT INTO `tb_option` VALUES (98, 4, '34.我的想象力非常丰富');
INSERT INTO `tb_option` VALUES (99, 4, '35.我喜欢参加社交与娱乐聚会');
INSERT INTO `tb_option` VALUES (100, 4, '36.我很少感到忧郁或沮丧');
INSERT INTO `tb_option` VALUES (101, 4, '37.做事讲究逻辑和条理是我的一个特点');
INSERT INTO `tb_option` VALUES (102, 4, '38.我经常为那些遭遇不幸的人感到难过');
INSERT INTO `tb_option` VALUES (103, 4, '39.我很愿意也很容易接受新事物、新观点、新想法');
INSERT INTO `tb_option` VALUES (104, 4, '40.我希望成为领导者而不是被领导者');
INSERT INTO `tb_option` VALUES (105, 5, '1.无法预料的事情会让我非常不安');
INSERT INTO `tb_option` VALUES (106, 5, '2.没有获得我需要的全部信息会让我很沮丧');
INSERT INTO `tb_option` VALUES (107, 5, '3.一个人应该总是向前看，同时避免意外');
INSERT INTO `tb_option` VALUES (108, 5, '4.即使有最好的计划也会被一个不可预见的小事毁掉一切 ');
INSERT INTO `tb_option` VALUES (109, 5, '5.我一直想知道我的未来是什么');
INSERT INTO `tb_option` VALUES (110, 5, '6.我无法忍受突发状况');
INSERT INTO `tb_option` VALUES (111, 5, '7.我应该能提前安排好一切 ');
INSERT INTO `tb_option` VALUES (112, 5, '8.不确定性使我无法过上充实的生活 ');
INSERT INTO `tb_option` VALUES (113, 5, '9.到了该行动的时候，不确定性使我无法正常工作 ');
INSERT INTO `tb_option` VALUES (114, 5, '10.当我不确定时，我不能做得很好');
INSERT INTO `tb_option` VALUES (115, 5, '11.任何的疑惑都会阻止我行动');
INSERT INTO `tb_option` VALUES (116, 5, '12.我必须摆脱所有不确定的情况');

-- ----------------------------
-- Table structure for tb_option_select
-- ----------------------------
DROP TABLE IF EXISTS `tb_option_select`;
CREATE TABLE `tb_option_select`  (
  `id` int NOT NULL,
  `questionnaire_id` int NOT NULL,
  `content` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `score` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `question_option_select`(`questionnaire_id`) USING BTREE,
  CONSTRAINT `question_option_select` FOREIGN KEY (`questionnaire_id`) REFERENCES `tb_questionnaire` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of tb_option_select
-- ----------------------------
INSERT INTO `tb_option_select` VALUES (1, 1, '是', 4);
INSERT INTO `tb_option_select` VALUES (2, 1, '有时', 2);
INSERT INTO `tb_option_select` VALUES (3, 1, '否', 0);
INSERT INTO `tb_option_select` VALUES (4, 2, '不符合', 0);
INSERT INTO `tb_option_select` VALUES (5, 2, '有时符合', 1);
INSERT INTO `tb_option_select` VALUES (6, 2, '经常符合', 2);
INSERT INTO `tb_option_select` VALUES (7, 2, '总是符合', 3);
INSERT INTO `tb_option_select` VALUES (8, 3, '极少', 0);
INSERT INTO `tb_option_select` VALUES (9, 3, '较少', 1);
INSERT INTO `tb_option_select` VALUES (10, 3, '中等', 2);
INSERT INTO `tb_option_select` VALUES (11, 3, '较多', 3);
INSERT INTO `tb_option_select` VALUES (12, 3, '很多', 4);
INSERT INTO `tb_option_select` VALUES (13, 4, '完全不符', 0);
INSERT INTO `tb_option_select` VALUES (14, 4, '大部分不符合', 1);
INSERT INTO `tb_option_select` VALUES (15, 4, '有点不符合', 2);
INSERT INTO `tb_option_select` VALUES (16, 4, '有点符合', 3);
INSERT INTO `tb_option_select` VALUES (17, 4, '大部分符合', 4);
INSERT INTO `tb_option_select` VALUES (18, 4, '完全符合', 5);
INSERT INTO `tb_option_select` VALUES (19, 5, '完全不符', 1);
INSERT INTO `tb_option_select` VALUES (20, 5, '基本不符', 2);
INSERT INTO `tb_option_select` VALUES (21, 5, '基本符合', 3);
INSERT INTO `tb_option_select` VALUES (22, 5, '非常符合', 4);
INSERT INTO `tb_option_select` VALUES (23, 5, '完全符合', 5);

-- ----------------------------
-- Table structure for tb_ques_sleep
-- ----------------------------
DROP TABLE IF EXISTS `tb_ques_sleep`;
CREATE TABLE `tb_ques_sleep`  (
  `id` int NOT NULL,
  `questionnaire_id` int NOT NULL,
  `content` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `q1` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `q2` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `q3` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `q4` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `q5` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `tb_ques_sleep`(`questionnaire_id`) USING BTREE,
  CONSTRAINT `tb_ques_sleep` FOREIGN KEY (`questionnaire_id`) REFERENCES `tb_questionnaire` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tb_ques_sleep
-- ----------------------------
INSERT INTO `tb_ques_sleep` VALUES (1, 6, '1.在最近一个月中，您晚上上床睡觉通常是____点钟', '', '', '', '', NULL);
INSERT INTO `tb_ques_sleep` VALUES (2, 6, '2.在最近一个月中，您每晚通常要多长时间才能入睡（从上床到入睡）:____分钟', NULL, NULL, NULL, NULL, NULL);
INSERT INTO `tb_ques_sleep` VALUES (3, 6, '3.在最近一个月中，通常早上____点起床', NULL, NULL, NULL, NULL, NULL);
INSERT INTO `tb_ques_sleep` VALUES (4, 6, '4.在最近一个月中，您每晚实际睡眠的时间为____小时（注意不等于卧床时间）', NULL, NULL, NULL, NULL, NULL);
INSERT INTO `tb_ques_sleep` VALUES (5, 6, 'A. 不能在 30 分钟内入睡', '过去一个月没有', '每周平均不足一个晚上', '每周平均有一或两个晚上', '每周有平均三个或更多晚上', NULL);
INSERT INTO `tb_ques_sleep` VALUES (6, 6, 'B. 在晚上睡觉过程中醒来或者早醒（凌晨醒后不容易再次入睡）', '过去一个月没有', '每周平均不足一个晚上', '每周平均有一或两个晚上', '每周有平均三个或更多晚上', NULL);
INSERT INTO `tb_ques_sleep` VALUES (7, 6, 'C. 晚上起床上洗手间', '过去一个月没有', '每周平均不足一个晚上', '每周平均有一或两个晚上', '每周有平均三个或更多晚上', NULL);
INSERT INTO `tb_ques_sleep` VALUES (8, 6, 'D. 晚上睡觉时出现不舒服的呼吸', '过去一个月没有', '每周平均不足一个晚上', '每周平均有一或两个晚上', '每周有平均三个或更多晚上', NULL);
INSERT INTO `tb_ques_sleep` VALUES (9, 6, 'E. 晚上睡觉出现大声咳嗽或鼾声', '过去一个月没有', '每周平均不足一个晚上', '每周平均有一或两个晚上', '每周有平均三个或更多晚上', NULL);
INSERT INTO `tb_ques_sleep` VALUES (10, 6, 'F. 晚上睡觉感到寒冷', '过去一个月没有', '每周平均不足一个晚上', '每周平均有一或两个晚上', '每周有平均三个或更多晚上', NULL);
INSERT INTO `tb_ques_sleep` VALUES (11, 6, 'G. 晚上睡觉感到太热', '过去一个月没有', '每周平均不足一个晚上', '每周平均有一或两个晚上', '每周有平均三个或更多晚上', NULL);
INSERT INTO `tb_ques_sleep` VALUES (12, 6, 'H. 晚上睡觉做噩梦', '过去一个月没有', '每周平均不足一个晚上', '每周平均有一或两个晚上', '每周有平均三个或更多晚上', NULL);
INSERT INTO `tb_ques_sleep` VALUES (13, 6, 'I. 晚上睡觉身上出现疼痛不适', '过去一个月没有', '每周平均不足一个晚上', '每周平均有一或两个晚上', '每周有平均三个或更多晚上', NULL);
INSERT INTO `tb_ques_sleep` VALUES (14, 6, 'J. 其他影响睡眠的问题和原因，', '过去一个月没有', '每周平均不足一个晚上', '每周平均有一或两个晚上', '每周有平均三个或更多晚上', NULL);
INSERT INTO `tb_ques_sleep` VALUES (15, 6, '⒍在最近一个月中，总的来说，您认为自己的睡眠质量', '很好', '较好', '较差', '很差', NULL);
INSERT INTO `tb_ques_sleep` VALUES (16, 6, '⒎在最近一个月中，您是否要服用药物才能入睡', '过去一个月没有', '每周平均不足一个晚上', '每周平均有一或两个晚上', '每周有平均三个或更多晚上', NULL);
INSERT INTO `tb_ques_sleep` VALUES (17, 6, '⒏在最近一个月中，您是否在开车、吃饭或参加社会活动时时常感到困倦', '过去一个月没有', '每周平均不足一个晚上', '每周平均有一或两个晚上', '每周有平均三个或更多晚上', NULL);
INSERT INTO `tb_ques_sleep` VALUES (18, 6, '⒐在最近一个月中，您在做事情时是否感到精力不足', '过去一个月没有', '每周平均不足一个晚上', '每周平均有一或两个晚上', '每周有平均三个或更多晚上', NULL);

-- ----------------------------
-- Table structure for tb_questionnaire
-- ----------------------------
DROP TABLE IF EXISTS `tb_questionnaire`;
CREATE TABLE `tb_questionnaire`  (
  `id` int NOT NULL,
  `publish_time` datetime NOT NULL,
  `title` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `score` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of tb_questionnaire
-- ----------------------------
INSERT INTO `tb_questionnaire` VALUES (1, '2021-07-06 13:20:00', '表1', 25);
INSERT INTO `tb_questionnaire` VALUES (2, '2021-07-06 13:41:43', '表2', 21);
INSERT INTO `tb_questionnaire` VALUES (3, '2021-07-21 13:41:59', '表3', 18);
INSERT INTO `tb_questionnaire` VALUES (4, '2021-07-15 13:42:23', '表4', 40);
INSERT INTO `tb_questionnaire` VALUES (5, '2021-08-06 16:11:33', '表5', 12);
INSERT INTO `tb_questionnaire` VALUES (6, '2021-08-06 16:17:38', '表6', 18);

-- ----------------------------
-- Table structure for tb_record
-- ----------------------------
DROP TABLE IF EXISTS `tb_record`;
CREATE TABLE `tb_record`  (
  `score_1` int NOT NULL,
  `score_2_1` int NOT NULL,
  `score_2_2` int NOT NULL,
  `score_2_3` int NOT NULL,
  `score_3` int NOT NULL,
  `score_4_1` int NOT NULL,
  `score_4_2` int NOT NULL,
  `score_4_3` int NOT NULL,
  `score_4_4` int NOT NULL,
  `score_4_5` int NOT NULL,
  `score_5_1` int NOT NULL,
  `score_5_2` int NOT NULL,
  `score_5_3` int NOT NULL,
  `score_6` int NOT NULL,
  `finish_time` datetime NOT NULL,
  `openid` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`openid`) USING BTREE,
  CONSTRAINT `account_record` FOREIGN KEY (`openid`) REFERENCES `tb_account` (`openid`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of tb_record
-- ----------------------------

SET FOREIGN_KEY_CHECKS = 1;
