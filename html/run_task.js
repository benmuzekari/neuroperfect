/***************** 
 * Run_Task Test *
 *****************/

import { PsychoJS } from './lib/core-2020.2.js';
import * as core from './lib/core-2020.2.js';
import { TrialHandler } from './lib/data-2020.2.js';
import { Scheduler } from './lib/util-2020.2.js';
import * as visual from './lib/visual-2020.2.js';
import * as sound from './lib/sound-2020.2.js';
import * as util from './lib/util-2020.2.js';
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([(- 0.9), (- 0.9), (- 0.9)]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'run_task';  // from the Builder filename that created this script
let expInfo = {'participant': ''};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(initialize_stim_and_key_variablesRoutineBegin());
flowScheduler.add(initialize_stim_and_key_variablesRoutineEachFrame());
flowScheduler.add(initialize_stim_and_key_variablesRoutineEnd());
flowScheduler.add(get_emailRoutineBegin());
flowScheduler.add(get_emailRoutineEachFrame());
flowScheduler.add(get_emailRoutineEnd());
flowScheduler.add(welcome_slideRoutineBegin());
flowScheduler.add(welcome_slideRoutineEachFrame());
flowScheduler.add(welcome_slideRoutineEnd());
flowScheduler.add(SAM_hu_directionsRoutineBegin());
flowScheduler.add(SAM_hu_directionsRoutineEachFrame());
flowScheduler.add(SAM_hu_directionsRoutineEnd());
flowScheduler.add(SAM_hu_questionRoutineBegin());
flowScheduler.add(SAM_hu_questionRoutineEachFrame());
flowScheduler.add(SAM_hu_questionRoutineEnd());
flowScheduler.add(highlight_sam_hu_pre_choiceRoutineBegin());
flowScheduler.add(highlight_sam_hu_pre_choiceRoutineEachFrame());
flowScheduler.add(highlight_sam_hu_pre_choiceRoutineEnd());
flowScheduler.add(SAM_ec_directionsRoutineBegin());
flowScheduler.add(SAM_ec_directionsRoutineEachFrame());
flowScheduler.add(SAM_ec_directionsRoutineEnd());
flowScheduler.add(SAM_ec_questionRoutineBegin());
flowScheduler.add(SAM_ec_questionRoutineEachFrame());
flowScheduler.add(SAM_ec_questionRoutineEnd());
flowScheduler.add(highlight_sam_ec_pre_choiceRoutineBegin());
flowScheduler.add(highlight_sam_ec_pre_choiceRoutineEachFrame());
flowScheduler.add(highlight_sam_ec_pre_choiceRoutineEnd());
flowScheduler.add(introduce_keyboard_hand_positioningRoutineBegin());
flowScheduler.add(introduce_keyboard_hand_positioningRoutineEachFrame());
flowScheduler.add(introduce_keyboard_hand_positioningRoutineEnd());
flowScheduler.add(begin_instructionsRoutineBegin());
flowScheduler.add(begin_instructionsRoutineEachFrame());
flowScheduler.add(begin_instructionsRoutineEnd());
flowScheduler.add(continue_beginRoutineBegin());
flowScheduler.add(continue_beginRoutineEachFrame());
flowScheduler.add(continue_beginRoutineEnd());
flowScheduler.add(slide_max_pointsRoutineBegin());
flowScheduler.add(slide_max_pointsRoutineEachFrame());
flowScheduler.add(slide_max_pointsRoutineEnd());
flowScheduler.add(fractal_selection_quizRoutineBegin());
flowScheduler.add(fractal_selection_quizRoutineEachFrame());
flowScheduler.add(fractal_selection_quizRoutineEnd());
flowScheduler.add(fractal_reminder_showRoutineBegin());
flowScheduler.add(fractal_reminder_showRoutineEachFrame());
flowScheduler.add(fractal_reminder_showRoutineEnd());
flowScheduler.add(draw_slide_3RoutineBegin());
flowScheduler.add(draw_slide_3RoutineEachFrame());
flowScheduler.add(draw_slide_3RoutineEnd());
flowScheduler.add(display_feedback_meaningsRoutineBegin());
flowScheduler.add(display_feedback_meaningsRoutineEachFrame());
flowScheduler.add(display_feedback_meaningsRoutineEnd());
flowScheduler.add(first_quiz_first_questionRoutineBegin());
flowScheduler.add(first_quiz_first_questionRoutineEachFrame());
flowScheduler.add(first_quiz_first_questionRoutineEnd());
flowScheduler.add(first_quiz_first_question_reminderRoutineBegin());
flowScheduler.add(first_quiz_first_question_reminderRoutineEachFrame());
flowScheduler.add(first_quiz_first_question_reminderRoutineEnd());
flowScheduler.add(first_quiz_second_questionRoutineBegin());
flowScheduler.add(first_quiz_second_questionRoutineEachFrame());
flowScheduler.add(first_quiz_second_questionRoutineEnd());
flowScheduler.add(first_quiz_second_question_reminderRoutineBegin());
flowScheduler.add(first_quiz_second_question_reminderRoutineEachFrame());
flowScheduler.add(first_quiz_second_question_reminderRoutineEnd());
flowScheduler.add(first_quiz_third_questionRoutineBegin());
flowScheduler.add(first_quiz_third_questionRoutineEachFrame());
flowScheduler.add(first_quiz_third_questionRoutineEnd());
flowScheduler.add(first_quiz_third_question_reminderRoutineBegin());
flowScheduler.add(first_quiz_third_question_reminderRoutineEachFrame());
flowScheduler.add(first_quiz_third_question_reminderRoutineEnd());
flowScheduler.add(total_reminder_oneRoutineBegin());
flowScheduler.add(total_reminder_oneRoutineEachFrame());
flowScheduler.add(total_reminder_oneRoutineEnd());
flowScheduler.add(continue_instructions_8_01RoutineBegin());
flowScheduler.add(continue_instructions_8_01RoutineEachFrame());
flowScheduler.add(continue_instructions_8_01RoutineEnd());
flowScheduler.add(continue_instructions_8_02RoutineBegin());
flowScheduler.add(continue_instructions_8_02RoutineEachFrame());
flowScheduler.add(continue_instructions_8_02RoutineEnd());
flowScheduler.add(continue_instructions_8_03RoutineBegin());
flowScheduler.add(continue_instructions_8_03RoutineEachFrame());
flowScheduler.add(continue_instructions_8_03RoutineEnd());
flowScheduler.add(feedback_selection_quizRoutineBegin());
flowScheduler.add(feedback_selection_quizRoutineEachFrame());
flowScheduler.add(feedback_selection_quizRoutineEnd());
flowScheduler.add(feedback_post_quiz_reminderRoutineBegin());
flowScheduler.add(feedback_post_quiz_reminderRoutineEachFrame());
flowScheduler.add(feedback_post_quiz_reminderRoutineEnd());
flowScheduler.add(continue_slide_09_01RoutineBegin());
flowScheduler.add(continue_slide_09_01RoutineEachFrame());
flowScheduler.add(continue_slide_09_01RoutineEnd());
flowScheduler.add(continue_slide_09_02RoutineBegin());
flowScheduler.add(continue_slide_09_02RoutineEachFrame());
flowScheduler.add(continue_slide_09_02RoutineEnd());
flowScheduler.add(continue_slide_10_01RoutineBegin());
flowScheduler.add(continue_slide_10_01RoutineEachFrame());
flowScheduler.add(continue_slide_10_01RoutineEnd());
flowScheduler.add(continue_slide_10_02RoutineBegin());
flowScheduler.add(continue_slide_10_02RoutineEachFrame());
flowScheduler.add(continue_slide_10_02RoutineEnd());
flowScheduler.add(attention_shape_checkRoutineBegin());
flowScheduler.add(attention_shape_checkRoutineEachFrame());
flowScheduler.add(attention_shape_checkRoutineEnd());
flowScheduler.add(attention_reminderRoutineBegin());
flowScheduler.add(attention_reminderRoutineEachFrame());
flowScheduler.add(attention_reminderRoutineEnd());
flowScheduler.add(continue_instructions_even_further_11RoutineBegin());
flowScheduler.add(continue_instructions_even_further_11RoutineEachFrame());
flowScheduler.add(continue_instructions_even_further_11RoutineEnd());
flowScheduler.add(calib_oneRoutineBegin());
flowScheduler.add(calib_oneRoutineEachFrame());
flowScheduler.add(calib_oneRoutineEnd());
flowScheduler.add(calib_lastRoutineBegin());
flowScheduler.add(calib_lastRoutineEachFrame());
flowScheduler.add(calib_lastRoutineEnd());
flowScheduler.add(advance_to_practice_sessionRoutineBegin());
flowScheduler.add(advance_to_practice_sessionRoutineEachFrame());
flowScheduler.add(advance_to_practice_sessionRoutineEnd());
const prac_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(prac_trialsLoopBegin, prac_trialsLoopScheduler);
flowScheduler.add(prac_trialsLoopScheduler);
flowScheduler.add(prac_trialsLoopEnd);
flowScheduler.add(blank_screen_2RoutineBegin());
flowScheduler.add(blank_screen_2RoutineEachFrame());
flowScheduler.add(blank_screen_2RoutineEnd());
flowScheduler.add(second_quizRoutineBegin());
flowScheduler.add(second_quizRoutineEachFrame());
flowScheduler.add(second_quizRoutineEnd());
flowScheduler.add(second_quiz_first_questionRoutineBegin());
flowScheduler.add(second_quiz_first_questionRoutineEachFrame());
flowScheduler.add(second_quiz_first_questionRoutineEnd());
flowScheduler.add(second_quiz_first_question_reminderRoutineBegin());
flowScheduler.add(second_quiz_first_question_reminderRoutineEachFrame());
flowScheduler.add(second_quiz_first_question_reminderRoutineEnd());
flowScheduler.add(second_quiz_second_questionRoutineBegin());
flowScheduler.add(second_quiz_second_questionRoutineEachFrame());
flowScheduler.add(second_quiz_second_questionRoutineEnd());
flowScheduler.add(second_quiz_second_question_reminderRoutineBegin());
flowScheduler.add(second_quiz_second_question_reminderRoutineEachFrame());
flowScheduler.add(second_quiz_second_question_reminderRoutineEnd());
flowScheduler.add(second_quiz_third_questionRoutineBegin());
flowScheduler.add(second_quiz_third_questionRoutineEachFrame());
flowScheduler.add(second_quiz_third_questionRoutineEnd());
flowScheduler.add(second_quiz_third_question_reminderRoutineBegin());
flowScheduler.add(second_quiz_third_question_reminderRoutineEachFrame());
flowScheduler.add(second_quiz_third_question_reminderRoutineEnd());
flowScheduler.add(last_stim_reminderRoutineBegin());
flowScheduler.add(last_stim_reminderRoutineEachFrame());
flowScheduler.add(last_stim_reminderRoutineEnd());
flowScheduler.add(advance_to_main_taskRoutineBegin());
flowScheduler.add(advance_to_main_taskRoutineEachFrame());
flowScheduler.add(advance_to_main_taskRoutineEnd());
const main_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(main_trialsLoopBegin, main_trialsLoopScheduler);
flowScheduler.add(main_trialsLoopScheduler);
flowScheduler.add(main_trialsLoopEnd);
flowScheduler.add(blank_screen_2RoutineBegin());
flowScheduler.add(blank_screen_2RoutineEachFrame());
flowScheduler.add(blank_screen_2RoutineEnd());
flowScheduler.add(completed_main_taskRoutineBegin());
flowScheduler.add(completed_main_taskRoutineEachFrame());
flowScheduler.add(completed_main_taskRoutineEnd());
flowScheduler.add(continue_to_fractal_questionRoutineBegin());
flowScheduler.add(continue_to_fractal_questionRoutineEachFrame());
flowScheduler.add(continue_to_fractal_questionRoutineEnd());
flowScheduler.add(post_task_fractal_questionRoutineBegin());
flowScheduler.add(post_task_fractal_questionRoutineEachFrame());
flowScheduler.add(post_task_fractal_questionRoutineEnd());
flowScheduler.add(SAM_hu_directionsRoutineBegin());
flowScheduler.add(SAM_hu_directionsRoutineEachFrame());
flowScheduler.add(SAM_hu_directionsRoutineEnd());
flowScheduler.add(SAM_hu_question_2RoutineBegin());
flowScheduler.add(SAM_hu_question_2RoutineEachFrame());
flowScheduler.add(SAM_hu_question_2RoutineEnd());
flowScheduler.add(highlight_post_sam_huRoutineBegin());
flowScheduler.add(highlight_post_sam_huRoutineEachFrame());
flowScheduler.add(highlight_post_sam_huRoutineEnd());
flowScheduler.add(SAM_ec_directionsRoutineBegin());
flowScheduler.add(SAM_ec_directionsRoutineEachFrame());
flowScheduler.add(SAM_ec_directionsRoutineEnd());
flowScheduler.add(SAM_ec_question_2RoutineBegin());
flowScheduler.add(SAM_ec_question_2RoutineEachFrame());
flowScheduler.add(SAM_ec_question_2RoutineEnd());
flowScheduler.add(highlight_sam_ec_post_choiceRoutineBegin());
flowScheduler.add(highlight_sam_ec_post_choiceRoutineEachFrame());
flowScheduler.add(highlight_sam_ec_post_choiceRoutineEnd());
flowScheduler.add(total_points_end_experimentRoutineBegin());
flowScheduler.add(total_points_end_experimentRoutineEachFrame());
flowScheduler.add(total_points_end_experimentRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.DEBUG);


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.2.4';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  psychoJS.setRedirectUrls('https://duke.qualtrics.com/jfe/form/SV_3K0QGy58pfeZaWF?id=24481', 'https://duke.qualtrics.com/jfe/form/SV_3K0QGy58pfeZaWF?id=24481');

  return Scheduler.Event.NEXT;
}


var initialize_stim_and_key_variablesClock;
var kb;
var timer;
var win;
var keys_event;
var random;
var event;
var randint;
var condition;
var excel_sheet_choice_practice;
var excel_sheet_choice_main;
var instruction_slide_2_selection;
var select_key_to_press;
var select_feedback_to_press;
var random_feedback_stim;
var post_task_fractal_selection;
var participant;
var instructions_slide_one;
var instructions_slide_two;
var instructions_slide_two_second;
var instructions_slide_three;
var instructions_slide_four;
var instructions_slide_five;
var instructions_slide_six;
var instructions_slide_seven;
var instructions_slide_8_01;
var instructions_slide_8_02;
var instructions_slide_8_03;
var instructions_slide_09_01;
var instructions_slide_09_02;
var instructions_slide_10_01;
var instructions_slide_10_02;
var instructions_slide_eleven;
var instructions_slide_twelve;
var instructions_slide_thirteen;
var instructions_slide_fourteen;
var max_points;
var intro_to_kb;
var intro_to_kb_old;
var horizontal_feedback_stim;
var vertical_feedback_stim;
var grey_no_feedback_stim;
var feedback_choice_screen;
var feedback_no_screen;
var feedback_yes_screen;
var fractal_blossom;
var fractal_octopus;
var calibration_slide_1;
var calibration_slide_2;
var calibration_slide_3;
var calibration_slide_4;
var calibration_slide_5;
var calibration_slide_6;
var calibration_slide_7;
var calibration_slide_8;
var calibration_slide_9;
var calibration_slide_10;
var calibration_slide_11;
var calibration_slide_12;
var calibration_slide_13;
var post_task_completion_slide;
var post_task_continue_slide;
var post_task_fractal_slide;
var post_task_fractal_1_selected_slide;
var post_task_fractal_2_selected_slide;
var correct_feedback_reminder;
var correct_fractal_reminder;
var correct_result_no_feedback;
var correct_result_plus_one;
var correct_result_plus_zero;
var correct_shape;
var incorrect_feedback_reminder;
var incorrect_fractal_reminder;
var incorrect_result_no_feedback;
var incorrect_result_plus_one;
var incorrect_result_plus_zero;
var incorrect_shape;
var press_fractal_left;
var press_fractal_right;
var press_no_feedback;
var press_yes_feedback;
var result_final_reminder;
var shapes_question;
var blank_screen_image_black;
var get_emailClock;
var email_instructions;
var textbox_email;
var enter_email;
var submit_text;
var welcome_slideClock;
var slide_1_inst;
var welcome_slide_key_resp;
var SAM_hu_directionsClock;
var SAM_hu_instructions;
var SAM_hu_instructions_key_resp;
var SAM_hu_questionClock;
var SAM_hu;
var choice_1;
var choice_2;
var choice_3;
var choice_4;
var choice_5;
var choice_6;
var choice_7;
var choice_8;
var choice_9;
var select_answer_mouse_sam_hu;
var highlight_sam_hu_pre_choiceClock;
var Sam_hu_highlight_pre;
var SAM_ec_directionsClock;
var SAM_ec_instructions;
var SAM_ec_instructions_key_resp;
var SAM_ec_questionClock;
var SAM_ec;
var choice_num_1;
var choice_num_2;
var choice_num_3;
var choice_num_4;
var choice_num_5;
var choice_num_6;
var choice_num_7;
var choice_num_8;
var choice_num_9;
var select_answer_mouse_sam_ec;
var highlight_sam_ec_pre_choiceClock;
var sam_ec_pre_highlight;
var introduce_keyboard_hand_positioningClock;
var draw_kb_key_resp;
var begin_instructionsClock;
var begin_task_instructions_key_resp;
var continue_beginClock;
var slide_two_key_response;
var slide_max_pointsClock;
var max_points_slide_key_resp;
var fractal_selection_quizClock;
var select_key_to_press_slide;
var key_to_press_outcome;
var fractal_selection_quiz_key_resp;
var fractal_reminder_showClock;
var fractal_reminder_show_key_resp;
var draw_slide_3Clock;
var slide_3_key_resp;
var display_feedback_meaningsClock;
var display_feedback_meanings_key_resp;
var first_quiz_first_questionClock;
var first_stim_quiz_first_question_result;
var first_stim_quiz_second_question_result;
var first_stim_quiz_third_question_result;
var first_quiz_first_question_key_resp;
var first_quiz_first_question_reminderClock;
var first_quiz_first_q_reminder_key_resp;
var first_quiz_second_questionClock;
var first_quiz_second_question_key_resp;
var first_quiz_second_question_reminderClock;
var first_quiz_second_question_reminder_key_resp;
var first_quiz_third_questionClock;
var last_q_first_quiz_key_resp;
var first_quiz_third_question_reminderClock;
var first_quiz_third_question_reminder_key_resp;
var total_reminder_oneClock;
var first_reminder_key_resp;
var continue_instructions_8_01Clock;
var slide_8_01_key_resp;
var continue_instructions_8_02Clock;
var slide_8_02_key_resp;
var continue_instructions_8_03Clock;
var slide_8_03_key_resp;
var feedback_selection_quizClock;
var select_feedback_to_press_slide;
var feedback_to_press_outcome;
var feedback_selection_quiz_key_resp;
var feedback_post_quiz_reminderClock;
var feedback_post_quiz_reminder_key_resp;
var continue_slide_09_01Clock;
var slide_09_01_key_resp;
var continue_slide_09_02Clock;
var slide_09_02_key_resp;
var continue_slide_10_01Clock;
var slide_10_01_key_resp;
var continue_slide_10_02Clock;
var slide_10_02_key_resp;
var attention_shape_checkClock;
var shape_quiz_result;
var get_shape_response;
var attention_reminderClock;
var attention_reminder_key_resp;
var continue_instructions_even_further_11Clock;
var slide_11_key_resp;
var calib_oneClock;
var calib_one_space;
var calib_lastClock;
var calibration_space_bar_press;
var advance_to_practice_sessionClock;
var enter_to_practice_session;
var practice_taskClock;
var prac_trial_num;
var prac_total_points;
var iti_prac;
var fractal_one_prac;
var fractal_two_prac;
var key_resp_prac;
var isi_screenClock;
var isi_stim;
var missed_trial_logicClock;
var missed_trial_practice;
var no_feedback_work_logicClock;
var no_feedback_work_image;
var grey_work_for_fbClock;
var grey_stim_work_for_fb;
var ask_want_to_work_for_feedbackClock;
var feedback_choice_key_resp;
var feedback_choice_slide;
var no_fb_highlightClock;
var no_fb_slide;
var yes_fb_highlightClock;
var yes_fb_slide;
var fb_work_timeClock;
var draw_feedback_to_screenClock;
var work_for_feedback_space_bar_press;
var post_work_blankClock;
var blank_image;
var post_work_space_presses;
var end_loop_data_logClock;
var blank_screen_2Clock;
var blank_slide_2;
var second_quizClock;
var second_stim_quiz_first_question_result;
var second_stim_quiz_second_question_result;
var second_stim_quiz_third_question_result;
var start_second_quiz;
var second_quiz_first_questionClock;
var first_q_second_quiz_resp;
var second_quiz_first_question_reminderClock;
var advance_q_2_quiz_2;
var second_quiz_second_questionClock;
var resp_q_2_q_2;
var second_quiz_second_question_reminderClock;
var advance_q_3_quiz_2;
var second_quiz_third_questionClock;
var resp_quiz_2_q_3;
var second_quiz_third_question_reminderClock;
var advance_from_second_quiz;
var last_stim_reminderClock;
var advance_from_last_reminder;
var advance_to_main_taskClock;
var enter_main_game;
var main_taskClock;
var main_trial_num;
var main_total_points;
var iti_main;
var fractal_one_main;
var fractal_two_main;
var key_resp_main;
var completed_main_taskClock;
var post_task_image;
var continue_to_fractal_questionClock;
var go_to_fractal_question;
var post_task_fractal_questionClock;
var choose_fractal;
var SAM_hu_question_2Clock;
var SAM_hu_2;
var choice_1_post;
var choice_2_post;
var choice_3_post;
var choice_4_post;
var choice_5_post;
var choice_6_post;
var choice_7_post;
var choice_8_post;
var choice_9_post;
var select_answer_mouse_3;
var highlight_post_sam_huClock;
var sam_hu_highlight_post;
var SAM_ec_question_2Clock;
var SAM_ec_2;
var choice_num_1_post;
var choice_num_2_post;
var choice_num_3_post;
var choice_num_4_post;
var choice_num_5_post;
var choice_num_6_post;
var choice_num_7_post;
var choice_num_8_post;
var choice_num_9_post;
var select_answer_mouse_4;
var highlight_sam_ec_post_choiceClock;
var sam_ec_post_highlight;
var total_points_end_experimentClock;
var final_total_points;
var rest_of_text;
var exit_task;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "initialize_stim_and_key_variables"
  initialize_stim_and_key_variablesClock = new util.Clock();
  kb = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true}); 
  timer = new util.Clock;
  win = psychoJS.window;
  keys_event = psychoJS.eventManager.getKeys();
  random = Math.random;
  event = psychoJS.eventManager;
  randint = function(min, maxplusone) {
    return Math.floor(Math.random() * (maxplusone - min) ) + min;
  }
  
  condition = randint(1,3);
  excel_sheet_choice_practice = randint(1,3);
  excel_sheet_choice_main = randint(1,3);
  instruction_slide_2_selection = randint(1,3);
  select_key_to_press = randint(1,3);
  select_feedback_to_press = randint(1,3);
  random_feedback_stim = randint(1,3);
  post_task_fractal_selection = randint(1,3);
  
  participant = "n/a";
  quiz_and_attention_check_fails;
  instructions_slide_one = new visual.ImageStim({"win": win, "image": "instructions/Slide_01_instructions.png", "size": [1, 0.75]});
  instructions_slide_two = new visual.ImageStim({"win": win, "image": "instructions/Slide_02.1_instructions.png", "size": [1, 0.75]});
  instructions_slide_two_second = new visual.ImageStim({"win": win, "image": "instructions/Slide_02.2_instructions.png", "size": [1, 0.75]});
  instructions_slide_three = new visual.ImageStim({"win": win, "image": "instructions/Slide_03_instructions.png", "size": [1, 0.75]});
  instructions_slide_four = new visual.ImageStim({"win": win, "image": "instructions/Slide_04_instructions.png", "size": [1, 0.75]});
  instructions_slide_five = new visual.ImageStim({"win": win, "image": "instructions/Slide_05_instructions.png", "size": [1, 0.75]});
  instructions_slide_six = new visual.ImageStim({"win": win, "image": "instructions/Slide_06_instructions.png", "size": [1, 0.75]});
  instructions_slide_seven = new visual.ImageStim({"win": win, "image": "instructions/Slide_07.jpg", "size": [1, 0.75]});
  instructions_slide_8_01 = new visual.ImageStim({"win": win, "image": "instructions/Slide_08.1_instructions.png", "size": [1, 0.75]});
  instructions_slide_8_02 = new visual.ImageStim({"win": win, "image": "instructions/Slide_08.2_instructions.png", "size": [1, 0.75]});
  instructions_slide_8_03 = new visual.ImageStim({"win": win, "image": "instructions/Slide_08.3_instructions.png", "size": [1, 0.75]});
  instructions_slide_09_01 = new visual.ImageStim({"win": win, "image": "instructions/Slide_09.1_instructions.png", "size": [1, 0.75]});
  instructions_slide_09_02 = new visual.ImageStim({"win": win, "image": "instructions/Slide_09.2_instructions.png", "size": [1, 0.75]});
  instructions_slide_10_01 = new visual.ImageStim({"win": win, "image": "instructions/Slide_10.1_instructions.png", "size": [1.0, 0.75]});
  instructions_slide_10_02 = new visual.ImageStim({"win": win, "image": "instructions/Slide_10.2_instructions.png", "size": [1.0, 0.75]});
  instructions_slide_eleven = new visual.ImageStim({"win": win, "image": "instructions/Slide_11_instructions.png", "size": [1, 0.75]});
  instructions_slide_twelve = new visual.ImageStim({"win": win, "image": "instructions/Slide_12_instructions.png", "size": [1, 0.75]});
  instructions_slide_thirteen = new visual.ImageStim({"win": win, "image": "instructions/Slide_13_instructions.png", "size": [1, 0.75]});
  instructions_slide_fourteen = new visual.ImageStim({"win": win, "image": "instructions/Slide_14_instructions.png", "size": [1, 0.75]});
  max_points = new visual.ImageStim({"win": win, "image": "instructions/maximize_points.png", "size": [1, 0.75]});
  intro_to_kb = new visual.ImageStim({"win": win, "image": "instructions/introduce_keyboard.png", "size": [1, 0.75]});
  intro_to_kb_old = new visual.ImageStim({"win": win, "image": "instructions/introduce_kb.png", "size": [1, 0.75]});
  horizontal_feedback_stim = new visual.ImageStim({"win": win, "image": "stimuli/horizontal_feedback.png", "size": [0.15, 0.15]});
  vertical_feedback_stim = new visual.ImageStim({"win": win, "image": "stimuli/vertical_feedback.png", "size": [0.15, 0.15]});
  grey_no_feedback_stim = new visual.ImageStim({"win": win, "image": "stimuli/noninformative_feedback.png", "size": [0.15, 0.15]});
  feedback_choice_screen = new visual.ImageStim({"win": win, "image": "feedback_choice/feedback_choice.png", "size": [1, 0.75]});
  feedback_no_screen = new visual.ImageStim({"win": win, "image": "feedback_choice/feedback_no.png", "size": [1, 0.75]});
  feedback_yes_screen = new visual.ImageStim({"win": win, "image": "feedback_choice/feedback_yes.png", "size": [1, 0.75]});
  fractal_blossom = new visual.ImageStim({"win": win, "image": "stimuli/fractal_blossom.png", "size": [0.15, 0.15]});
  fractal_octopus = new visual.ImageStim({"win": win, "image": "stimuli/fractal_octopus.png", "size": [0.15, 0.15]});
  calibration_slide_1 = new visual.ImageStim({"win": win, "image": "calibration/slide1.png", "size": [1, 0.75]});
  calibration_slide_2 = new visual.ImageStim({"win": win, "image": "calibration/slide2.png", "size": [1, 0.75]});
  calibration_slide_3 = new visual.ImageStim({"win": win, "image": "calibration/slide3.png", "size": [1, 0.75]});
  calibration_slide_4 = new visual.ImageStim({"win": win, "image": "calibration/slide4.png", "size": [1, 0.75]});
  calibration_slide_5 = new visual.ImageStim({"win": win, "image": "calibration/slide5.png", "size": [1, 0.75]});
  calibration_slide_6 = new visual.ImageStim({"win": win, "image": "calibration/slide6.png", "size": [1, 0.75]});
  calibration_slide_7 = new visual.ImageStim({"win": win, "image": "calibration/slide7.png", "size": [1, 0.75]});
  calibration_slide_8 = new visual.ImageStim({"win": win, "image": "calibration/slide8.png", "size": [1, 0.75]});
  calibration_slide_9 = new visual.ImageStim({"win": win, "image": "calibration/slide9.png", "size": [1, 0.75]});
  calibration_slide_10 = new visual.ImageStim({"win": win, "image": "calibration/slide10.png", "size": [1, 0.75]});
  calibration_slide_11 = new visual.ImageStim({"win": win, "image": "calibration/slide11.png", "size": [1, 0.75]});
  calibration_slide_12 = new visual.ImageStim({"win": win, "image": "calibration/slide12.png", "size": [1, 0.75]});
  calibration_slide_13 = new visual.ImageStim({"win": win, "image": "calibration/slide13.png", "size": [1, 0.75]});
  post_task_completion_slide = new visual.ImageStim({"win": win, "image": "post_task/Slide_15.jpg", "size": [1, 0.75]});
  post_task_continue_slide = new visual.ImageStim({"win": win, "image": "post_task/Slide_16.jpg", "size": [1, 0.75]});
  post_task_fractal_slide = new visual.ImageStim({"win": win, "image": "post_task/Slide_17.jpg", "size": [1, 0.75]});
  post_task_fractal_1_selected_slide = new visual.ImageStim({"win": win, "image": "post_task/Slide_18.jpg", "size": [1, 0.75]});
  post_task_fractal_2_selected_slide = new visual.ImageStim({"win": win, "image": "post_task/Slide_19.jpg", "size": [1, 0.75]});
  correct_feedback_reminder = new visual.ImageStim({"win": win, "image": "comprehension_checks/correct_feedback_reminder.png", "size": [1, 0.75]});
  correct_fractal_reminder = new visual.ImageStim({"win": win, "image": "comprehension_checks/correct_fractal_reminder.png", "size": [1, 0.75]});
  correct_result_no_feedback = new visual.ImageStim({"win": win, "image": "comprehension_checks/correct_result_no_feedback.png", "size": [1, 0.75]});
  correct_result_plus_one = new visual.ImageStim({"win": win, "image": "comprehension_checks/correct_result_plus_one.png", "size": [1.0, 0.75]});
  correct_result_plus_zero = new visual.ImageStim({"win": win, "image": "comprehension_checks/correct_result_plus_zero.png", "size": [1, 0.75]});
  correct_shape = new visual.ImageStim({"win": win, "image": "comprehension_checks/correct_shape.png", "size": [1, 0.75]});
  incorrect_feedback_reminder = new visual.ImageStim({"win": win, "image": "comprehension_checks/incorrect_feedback_reminder.png", "size": [1, 0.75]});
  incorrect_fractal_reminder = new visual.ImageStim({"win": win, "image": "comprehension_checks/incorrect_fractal_reminder.png", "size": [1, 0.75]});
  incorrect_result_no_feedback = new visual.ImageStim({"win": win, "image": "comprehension_checks/incorrect_result_no_feedback.png", "size": [1, 0.75]});
  incorrect_result_plus_one = new visual.ImageStim({"win": win, "image": "comprehension_checks/incorrect_result_plus_one.png", "size": [1, 0.75]});
  incorrect_result_plus_zero = new visual.ImageStim({"win": win, "image": "comprehension_checks/incorrect_result_plus_zero.png", "size": [1, 0.75]});
  incorrect_shape = new visual.ImageStim({"win": win, "image": "comprehension_checks/incorrect_shape.png", "size": [1, 0.75]});
  press_fractal_left = new visual.ImageStim({"win": win, "image": "comprehension_checks/press_fractal_left.png", "size": [1, 0.75]});
  press_fractal_right = new visual.ImageStim({"win": win, "image": "comprehension_checks/press_fractal_right.png", "size": [1, 0.75]});
  press_no_feedback = new visual.ImageStim({"win": win, "image": "comprehension_checks/press_no_feedback.png", "size": [1, 0.75]});
  press_yes_feedback = new visual.ImageStim({"win": win, "image": "comprehension_checks/press_yes_feedback.png", "size": [1, 0.75]});
  result_final_reminder = new visual.ImageStim({"win": win, "image": "comprehension_checks/result_final_reminder.png", "size": [1, 0.75]});
  shapes_question = new visual.ImageStim({"win": win, "image": "comprehension_checks/attention_check_shapes.png", "size": [1, 0.75]});
  blank_screen_image_black = new visual.ImageStim({"win": win, "image": "stimuli/blank_screen.png", "size": [1, 0.75]});
  
  psychoJS.experiment.addData("condition", condition);
  psychoJS.experiment.addData("excel_sheet_choice_practice", excel_sheet_choice_practice);
  psychoJS.experiment.addData("excel_sheet_choice_main", excel_sheet_choice_main);
  psychoJS.experiment.addData("instruction_slide_2_selection", instruction_slide_2_selection);
  psychoJS.experiment.addData("select_key_to_press", select_key_to_press);
  psychoJS.experiment.addData("select_feedback_to_press", select_feedback_to_press);
  psychoJS.experiment.addData("random_feedback_stim", random_feedback_stim);
  psychoJS.experiment.addData("post_task_fractal_selection", post_task_fractal_selection);
  
  // Initialize components for Routine "get_email"
  get_emailClock = new util.Clock();
  email_instructions = new visual.TextStim({
    win: psychoJS.window,
    name: 'email_instructions',
    text: 'Please type your email below to recieve credit for this task:',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  textbox_email = new visual.TextBox({
    win: psychoJS.window,
    name: 'textbox_email',
    text: 'default text',
    font: 'Arial',
    pos: [0, 0.15], letterHeight: 0.05,
    size: undefined,  units: undefined, 
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    bold: false, italic: false,
    opacity: 1,
    padding: undefined,
    editable: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  enter_email = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  submit_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'submit_text',
    text: 'Press ENTER or RETURN to submit and continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.1)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "welcome_slide"
  welcome_slideClock = new util.Clock();
  slide_1_inst = new visual.ImageStim({
    win : psychoJS.window,
    name : 'slide_1_inst', units : undefined, 
    image : 'instructions/Slide_01_instructions.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [1, 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  welcome_slide_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SAM_hu_directions"
  SAM_hu_directionsClock = new util.Clock();
  SAM_hu_instructions = new visual.ImageStim({
    win : psychoJS.window,
    name : 'SAM_hu_instructions', units : undefined, 
    image : 'SAM/SAM_hu_ins.jpg', mask : undefined,
    ori : 0, pos : [0, 0], size : [1, 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  SAM_hu_instructions_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SAM_hu_question"
  SAM_hu_questionClock = new util.Clock();
  SAM_hu = new visual.ImageStim({
    win : psychoJS.window,
    name : 'SAM_hu', units : undefined, 
    image : 'SAM/SAM_hu.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [1, 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  choice_1 = new visual.Polygon ({
    win: psychoJS.window, name: 'choice_1', 
    edges: 100, size:[0.03, 0.03],
    ori: 0, pos: [(- 0.3), (- 0.18)],
    lineWidth: 1, lineColor: new util.Color([(- 0.9), (- 0.9), (- 0.9)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  choice_2 = new visual.Polygon ({
    win: psychoJS.window, name: 'choice_2', 
    edges: 100, size:[0.03, 0.03],
    ori: 0, pos: [(- 0.22), (- 0.18)],
    lineWidth: 1, lineColor: new util.Color([(- 0.9), (- 0.9), (- 0.9)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  choice_3 = new visual.Polygon ({
    win: psychoJS.window, name: 'choice_3', 
    edges: 100, size:[0.03, 0.03],
    ori: 0, pos: [(- 0.15), (- 0.18)],
    lineWidth: 1, lineColor: new util.Color([(- 0.9), (- 0.9), (- 0.9)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  choice_4 = new visual.Polygon ({
    win: psychoJS.window, name: 'choice_4', 
    edges: 100, size:[0.03, 0.03],
    ori: 0, pos: [(- 0.07), (- 0.18)],
    lineWidth: 1, lineColor: new util.Color([(- 0.9), (- 0.9), (- 0.9)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -4, interpolate: true,
  });
  
  choice_5 = new visual.Polygon ({
    win: psychoJS.window, name: 'choice_5', 
    edges: 100, size:[0.03, 0.03],
    ori: 0, pos: [0, (- 0.18)],
    lineWidth: 1, lineColor: new util.Color([(- 0.9), (- 0.9), (- 0.9)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -5, interpolate: true,
  });
  
  choice_6 = new visual.Polygon ({
    win: psychoJS.window, name: 'choice_6', 
    edges: 100, size:[0.03, 0.03],
    ori: 0, pos: [0.07, (- 0.18)],
    lineWidth: 1, lineColor: new util.Color([(- 0.9), (- 0.9), (- 0.9)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -6, interpolate: true,
  });
  
  choice_7 = new visual.Polygon ({
    win: psychoJS.window, name: 'choice_7', 
    edges: 100, size:[0.03, 0.03],
    ori: 0, pos: [0.15, (- 0.18)],
    lineWidth: 1, lineColor: new util.Color([(- 0.9), (- 0.9), (- 0.9)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -7, interpolate: true,
  });
  
  choice_8 = new visual.Polygon ({
    win: psychoJS.window, name: 'choice_8', 
    edges: 100, size:[0.03, 0.03],
    ori: 0, pos: [0.22, (- 0.18)],
    lineWidth: 1, lineColor: new util.Color([(- 0.9), (- 0.9), (- 0.9)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -8, interpolate: true,
  });
  
  choice_9 = new visual.Polygon ({
    win: psychoJS.window, name: 'choice_9', 
    edges: 100, size:[0.03, 0.03],
    ori: 0, pos: [0.3, (- 0.18)],
    lineWidth: 1, lineColor: new util.Color([(- 0.9), (- 0.9), (- 0.9)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -9, interpolate: true,
  });
  
  select_answer_mouse_sam_hu = new core.Mouse({
    win: psychoJS.window,
  });
  select_answer_mouse_sam_hu.mouseClock = new util.Clock();
  // Initialize components for Routine "highlight_sam_hu_pre_choice"
  highlight_sam_hu_pre_choiceClock = new util.Clock();
  Sam_hu_highlight_pre = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Sam_hu_highlight_pre', units : undefined, 
    image : 'SAM/SAM_hu.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [1, 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "SAM_ec_directions"
  SAM_ec_directionsClock = new util.Clock();
  SAM_ec_instructions = new visual.ImageStim({
    win : psychoJS.window,
    name : 'SAM_ec_instructions', units : undefined, 
    image : 'SAM/SAM_ec_ins.jpg', mask : undefined,
    ori : 0, pos : [0, 0], size : [1, 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  SAM_ec_instructions_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SAM_ec_question"
  SAM_ec_questionClock = new util.Clock();
  SAM_ec = new visual.ImageStim({
    win : psychoJS.window,
    name : 'SAM_ec', units : undefined, 
    image : 'SAM/SAM_ec.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [1, 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  choice_num_1 = new visual.Polygon ({
    win: psychoJS.window, name: 'choice_num_1', 
    edges: 100, size:[0.03, 0.03],
    ori: 0, pos: [(- 0.3), (- 0.18)],
    lineWidth: 1, lineColor: new util.Color([(- 0.9), (- 0.9), (- 0.9)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  choice_num_2 = new visual.Polygon ({
    win: psychoJS.window, name: 'choice_num_2', 
    edges: 100, size:[0.03, 0.03],
    ori: 0, pos: [(- 0.22), (- 0.18)],
    lineWidth: 1, lineColor: new util.Color([(- 0.9), (- 0.9), (- 0.9)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  choice_num_3 = new visual.Polygon ({
    win: psychoJS.window, name: 'choice_num_3', 
    edges: 100, size:[0.03, 0.03],
    ori: 0, pos: [(- 0.15), (- 0.18)],
    lineWidth: 1, lineColor: new util.Color([(- 0.9), (- 0.9), (- 0.9)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  choice_num_4 = new visual.Polygon ({
    win: psychoJS.window, name: 'choice_num_4', 
    edges: 100, size:[0.03, 0.03],
    ori: 0, pos: [(- 0.07), (- 0.18)],
    lineWidth: 1, lineColor: new util.Color([(- 0.9), (- 0.9), (- 0.9)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -4, interpolate: true,
  });
  
  choice_num_5 = new visual.Polygon ({
    win: psychoJS.window, name: 'choice_num_5', 
    edges: 100, size:[0.03, 0.03],
    ori: 0, pos: [0, (- 0.18)],
    lineWidth: 1, lineColor: new util.Color([(- 0.9), (- 0.9), (- 0.9)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -5, interpolate: true,
  });
  
  choice_num_6 = new visual.Polygon ({
    win: psychoJS.window, name: 'choice_num_6', 
    edges: 100, size:[0.03, 0.03],
    ori: 0, pos: [0.07, (- 0.18)],
    lineWidth: 1, lineColor: new util.Color([(- 0.9), (- 0.9), (- 0.9)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -6, interpolate: true,
  });
  
  choice_num_7 = new visual.Polygon ({
    win: psychoJS.window, name: 'choice_num_7', 
    edges: 100, size:[0.03, 0.03],
    ori: 0, pos: [0.15, (- 0.18)],
    lineWidth: 1, lineColor: new util.Color([(- 0.9), (- 0.9), (- 0.9)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -7, interpolate: true,
  });
  
  choice_num_8 = new visual.Polygon ({
    win: psychoJS.window, name: 'choice_num_8', 
    edges: 100, size:[0.03, 0.03],
    ori: 0, pos: [0.22, (- 0.18)],
    lineWidth: 1, lineColor: new util.Color([(- 0.9), (- 0.9), (- 0.9)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -8, interpolate: true,
  });
  
  choice_num_9 = new visual.Polygon ({
    win: psychoJS.window, name: 'choice_num_9', 
    edges: 100, size:[0.03, 0.03],
    ori: 0, pos: [0.3, (- 0.18)],
    lineWidth: 1, lineColor: new util.Color([(- 0.9), (- 0.9), (- 0.9)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -9, interpolate: true,
  });
  
  select_answer_mouse_sam_ec = new core.Mouse({
    win: psychoJS.window,
  });
  select_answer_mouse_sam_ec.mouseClock = new util.Clock();
  // Initialize components for Routine "highlight_sam_ec_pre_choice"
  highlight_sam_ec_pre_choiceClock = new util.Clock();
  sam_ec_pre_highlight = new visual.ImageStim({
    win : psychoJS.window,
    name : 'sam_ec_pre_highlight', units : undefined, 
    image : 'SAM/SAM_ec.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [1, 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "introduce_keyboard_hand_positioning"
  introduce_keyboard_hand_positioningClock = new util.Clock();
  draw_kb_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "begin_instructions"
  begin_instructionsClock = new util.Clock();
  begin_task_instructions_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "continue_begin"
  continue_beginClock = new util.Clock();
  slide_two_key_response = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "slide_max_points"
  slide_max_pointsClock = new util.Clock();
  max_points_slide_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fractal_selection_quiz"
  fractal_selection_quizClock = new util.Clock();
  select_key_to_press_slide = [];
  key_to_press_outcome = [];
  if ((select_key_to_press === 1)) {
      select_key_to_press_slide = press_fractal_left;
  } else {
      if ((select_key_to_press === 2)) {
          select_key_to_press_slide = press_fractal_right;
      }
  }
  
  fractal_selection_quiz_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fractal_reminder_show"
  fractal_reminder_showClock = new util.Clock();
  fractal_reminder_show_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "draw_slide_3"
  draw_slide_3Clock = new util.Clock();
  slide_3_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "display_feedback_meanings"
  display_feedback_meaningsClock = new util.Clock();
  display_feedback_meanings_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "first_quiz_first_question"
  first_quiz_first_questionClock = new util.Clock();
  first_stim_quiz_first_question_result = [];
  first_stim_quiz_second_question_result = [];
  first_stim_quiz_third_question_result = [];
  
  first_quiz_first_question_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "first_quiz_first_question_reminder"
  first_quiz_first_question_reminderClock = new util.Clock();
  first_quiz_first_q_reminder_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "first_quiz_second_question"
  first_quiz_second_questionClock = new util.Clock();
  first_quiz_second_question_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "first_quiz_second_question_reminder"
  first_quiz_second_question_reminderClock = new util.Clock();
  first_quiz_second_question_reminder_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "first_quiz_third_question"
  first_quiz_third_questionClock = new util.Clock();
  last_q_first_quiz_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "first_quiz_third_question_reminder"
  first_quiz_third_question_reminderClock = new util.Clock();
  first_quiz_third_question_reminder_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "total_reminder_one"
  total_reminder_oneClock = new util.Clock();
  first_reminder_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "continue_instructions_8_01"
  continue_instructions_8_01Clock = new util.Clock();
  slide_8_01_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "continue_instructions_8_02"
  continue_instructions_8_02Clock = new util.Clock();
  slide_8_02_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "continue_instructions_8_03"
  continue_instructions_8_03Clock = new util.Clock();
  slide_8_03_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "feedback_selection_quiz"
  feedback_selection_quizClock = new util.Clock();
  select_feedback_to_press_slide = [];
  feedback_to_press_outcome = [];
  if ((select_feedback_to_press === 1)) {
      select_feedback_to_press_slide = press_no_feedback;
  } else {
      if ((select_feedback_to_press === 2)) {
          select_feedback_to_press_slide = press_yes_feedback;
      }
  }
  
  feedback_selection_quiz_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "feedback_post_quiz_reminder"
  feedback_post_quiz_reminderClock = new util.Clock();
  feedback_post_quiz_reminder_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "continue_slide_09_01"
  continue_slide_09_01Clock = new util.Clock();
  slide_09_01_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "continue_slide_09_02"
  continue_slide_09_02Clock = new util.Clock();
  slide_09_02_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "continue_slide_10_01"
  continue_slide_10_01Clock = new util.Clock();
  slide_10_01_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "continue_slide_10_02"
  continue_slide_10_02Clock = new util.Clock();
  slide_10_02_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "attention_shape_check"
  attention_shape_checkClock = new util.Clock();
  shape_quiz_result = [];
  
  get_shape_response = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "attention_reminder"
  attention_reminderClock = new util.Clock();
  attention_reminder_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "continue_instructions_even_further_11"
  continue_instructions_even_further_11Clock = new util.Clock();
  slide_11_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "calib_one"
  calib_oneClock = new util.Clock();
  calib_one_space = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "calib_last"
  calib_lastClock = new util.Clock();
  calibration_space_bar_press = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "advance_to_practice_session"
  advance_to_practice_sessionClock = new util.Clock();
  enter_to_practice_session = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "practice_task"
  practice_taskClock = new util.Clock();
  prac_trial_num = 0;
  prac_total_points = 0;
  
  iti_prac = new visual.ShapeStim ({
    win: psychoJS.window, name: 'iti_prac', 
    vertices: 'cross', size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 0.01, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  fractal_one_prac = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fractal_one_prac', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -2.0 
  });
  fractal_two_prac = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fractal_two_prac', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -3.0 
  });
  key_resp_prac = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "isi_screen"
  isi_screenClock = new util.Clock();
  isi_stim = new visual.ShapeStim ({
    win: psychoJS.window, name: 'isi_stim', 
    vertices: 'cross', size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 0.01, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "missed_trial_logic"
  missed_trial_logicClock = new util.Clock();
  missed_trial_practice = new visual.TextStim({
    win: psychoJS.window,
    name: 'missed_trial_practice',
    text: 'No response recorded',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "no_feedback_work_logic"
  no_feedback_work_logicClock = new util.Clock();
  no_feedback_work_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'no_feedback_work_image', units : undefined, 
    image : load_feedback_stim_to_draw, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "grey_work_for_fb"
  grey_work_for_fbClock = new util.Clock();
  grey_stim_work_for_fb = new visual.ImageStim({
    win : psychoJS.window,
    name : 'grey_stim_work_for_fb', units : undefined, 
    image : load_feedback_stim_to_draw, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "ask_want_to_work_for_feedback"
  ask_want_to_work_for_feedbackClock = new util.Clock();
  feedback_choice_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  feedback_choice_slide = new visual.ImageStim({
    win : psychoJS.window,
    name : 'feedback_choice_slide', units : undefined, 
    image : 'feedback_choice/feedback_choice.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [1, 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "no_fb_highlight"
  no_fb_highlightClock = new util.Clock();
  no_fb_slide = new visual.ImageStim({
    win : psychoJS.window,
    name : 'no_fb_slide', units : undefined, 
    image : 'feedback_choice/feedback_no.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [1, 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "yes_fb_highlight"
  yes_fb_highlightClock = new util.Clock();
  yes_fb_slide = new visual.ImageStim({
    win : psychoJS.window,
    name : 'yes_fb_slide', units : undefined, 
    image : 'feedback_choice/feedback_yes.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [1, 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "fb_work_time"
  fb_work_timeClock = new util.Clock();
  // Initialize components for Routine "draw_feedback_to_screen"
  draw_feedback_to_screenClock = new util.Clock();
  work_for_feedback_space_bar_press = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "post_work_blank"
  post_work_blankClock = new util.Clock();
  blank_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'blank_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  post_work_space_presses = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "end_loop_data_log"
  end_loop_data_logClock = new util.Clock();
  // Initialize components for Routine "blank_screen_2"
  blank_screen_2Clock = new util.Clock();
  blank_slide_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'blank_slide_2',
    text: '       ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "second_quiz"
  second_quizClock = new util.Clock();
  second_stim_quiz_first_question_result = [];
  second_stim_quiz_second_question_result = [];
  second_stim_quiz_third_question_result = [];
  
  start_second_quiz = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "second_quiz_first_question"
  second_quiz_first_questionClock = new util.Clock();
  first_q_second_quiz_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "second_quiz_first_question_reminder"
  second_quiz_first_question_reminderClock = new util.Clock();
  advance_q_2_quiz_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "second_quiz_second_question"
  second_quiz_second_questionClock = new util.Clock();
  resp_q_2_q_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "second_quiz_second_question_reminder"
  second_quiz_second_question_reminderClock = new util.Clock();
  advance_q_3_quiz_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "second_quiz_third_question"
  second_quiz_third_questionClock = new util.Clock();
  resp_quiz_2_q_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "second_quiz_third_question_reminder"
  second_quiz_third_question_reminderClock = new util.Clock();
  advance_from_second_quiz = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "last_stim_reminder"
  last_stim_reminderClock = new util.Clock();
  advance_from_last_reminder = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "advance_to_main_task"
  advance_to_main_taskClock = new util.Clock();
  enter_main_game = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "main_task"
  main_taskClock = new util.Clock();
  main_trial_num = 0;
  main_total_points = 0;
  
  iti_main = new visual.ShapeStim ({
    win: psychoJS.window, name: 'iti_main', 
    vertices: 'cross', size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 0.01, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  fractal_one_main = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fractal_one_main', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -2.0 
  });
  fractal_two_main = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fractal_two_main', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -3.0 
  });
  key_resp_main = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "isi_screen"
  isi_screenClock = new util.Clock();
  isi_stim = new visual.ShapeStim ({
    win: psychoJS.window, name: 'isi_stim', 
    vertices: 'cross', size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 0.01, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "missed_trial_logic"
  missed_trial_logicClock = new util.Clock();
  missed_trial_practice = new visual.TextStim({
    win: psychoJS.window,
    name: 'missed_trial_practice',
    text: 'No response recorded',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "no_feedback_work_logic"
  no_feedback_work_logicClock = new util.Clock();
  no_feedback_work_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'no_feedback_work_image', units : undefined, 
    image : load_feedback_stim_to_draw, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "grey_work_for_fb"
  grey_work_for_fbClock = new util.Clock();
  grey_stim_work_for_fb = new visual.ImageStim({
    win : psychoJS.window,
    name : 'grey_stim_work_for_fb', units : undefined, 
    image : load_feedback_stim_to_draw, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "ask_want_to_work_for_feedback"
  ask_want_to_work_for_feedbackClock = new util.Clock();
  feedback_choice_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  feedback_choice_slide = new visual.ImageStim({
    win : psychoJS.window,
    name : 'feedback_choice_slide', units : undefined, 
    image : 'feedback_choice/feedback_choice.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [1, 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "no_fb_highlight"
  no_fb_highlightClock = new util.Clock();
  no_fb_slide = new visual.ImageStim({
    win : psychoJS.window,
    name : 'no_fb_slide', units : undefined, 
    image : 'feedback_choice/feedback_no.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [1, 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "yes_fb_highlight"
  yes_fb_highlightClock = new util.Clock();
  yes_fb_slide = new visual.ImageStim({
    win : psychoJS.window,
    name : 'yes_fb_slide', units : undefined, 
    image : 'feedback_choice/feedback_yes.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [1, 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "fb_work_time"
  fb_work_timeClock = new util.Clock();
  // Initialize components for Routine "draw_feedback_to_screen"
  draw_feedback_to_screenClock = new util.Clock();
  work_for_feedback_space_bar_press = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "post_work_blank"
  post_work_blankClock = new util.Clock();
  blank_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'blank_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  post_work_space_presses = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "end_loop_data_log"
  end_loop_data_logClock = new util.Clock();
  // Initialize components for Routine "blank_screen_2"
  blank_screen_2Clock = new util.Clock();
  blank_slide_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'blank_slide_2',
    text: '       ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "completed_main_task"
  completed_main_taskClock = new util.Clock();
  post_task_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'post_task_image', units : undefined, 
    image : 'post_task/Slide_15.jpg', mask : undefined,
    ori : 0, pos : [0, 0], size : [1, 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "continue_to_fractal_question"
  continue_to_fractal_questionClock = new util.Clock();
  go_to_fractal_question = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "post_task_fractal_question"
  post_task_fractal_questionClock = new util.Clock();
  choose_fractal = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SAM_hu_directions"
  SAM_hu_directionsClock = new util.Clock();
  SAM_hu_instructions = new visual.ImageStim({
    win : psychoJS.window,
    name : 'SAM_hu_instructions', units : undefined, 
    image : 'SAM/SAM_hu_ins.jpg', mask : undefined,
    ori : 0, pos : [0, 0], size : [1, 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  SAM_hu_instructions_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SAM_hu_question_2"
  SAM_hu_question_2Clock = new util.Clock();
  SAM_hu_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'SAM_hu_2', units : undefined, 
    image : 'SAM/SAM_hu.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [1, 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  choice_1_post = new visual.Polygon ({
    win: psychoJS.window, name: 'choice_1_post', 
    edges: 100, size:[0.03, 0.03],
    ori: 0, pos: [(- 0.3), (- 0.18)],
    lineWidth: 1, lineColor: new util.Color([(- 0.9), (- 0.9), (- 0.9)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  choice_2_post = new visual.Polygon ({
    win: psychoJS.window, name: 'choice_2_post', 
    edges: 100, size:[0.03, 0.03],
    ori: 0, pos: [(- 0.22), (- 0.18)],
    lineWidth: 1, lineColor: new util.Color([(- 0.9), (- 0.9), (- 0.9)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  choice_3_post = new visual.Polygon ({
    win: psychoJS.window, name: 'choice_3_post', 
    edges: 100, size:[0.03, 0.03],
    ori: 0, pos: [(- 0.15), (- 0.18)],
    lineWidth: 1, lineColor: new util.Color([(- 0.9), (- 0.9), (- 0.9)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  choice_4_post = new visual.Polygon ({
    win: psychoJS.window, name: 'choice_4_post', 
    edges: 100, size:[0.03, 0.03],
    ori: 0, pos: [(- 0.07), (- 0.18)],
    lineWidth: 1, lineColor: new util.Color([(- 0.9), (- 0.9), (- 0.9)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -4, interpolate: true,
  });
  
  choice_5_post = new visual.Polygon ({
    win: psychoJS.window, name: 'choice_5_post', 
    edges: 100, size:[0.03, 0.03],
    ori: 0, pos: [0, (- 0.18)],
    lineWidth: 1, lineColor: new util.Color([(- 0.9), (- 0.9), (- 0.9)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -5, interpolate: true,
  });
  
  choice_6_post = new visual.Polygon ({
    win: psychoJS.window, name: 'choice_6_post', 
    edges: 100, size:[0.03, 0.03],
    ori: 0, pos: [0.07, (- 0.18)],
    lineWidth: 1, lineColor: new util.Color([(- 0.9), (- 0.9), (- 0.9)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -6, interpolate: true,
  });
  
  choice_7_post = new visual.Polygon ({
    win: psychoJS.window, name: 'choice_7_post', 
    edges: 100, size:[0.03, 0.03],
    ori: 0, pos: [0.15, (- 0.18)],
    lineWidth: 1, lineColor: new util.Color([(- 0.9), (- 0.9), (- 0.9)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -7, interpolate: true,
  });
  
  choice_8_post = new visual.Polygon ({
    win: psychoJS.window, name: 'choice_8_post', 
    edges: 100, size:[0.03, 0.03],
    ori: 0, pos: [0.22, (- 0.18)],
    lineWidth: 1, lineColor: new util.Color([(- 0.9), (- 0.9), (- 0.9)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -8, interpolate: true,
  });
  
  choice_9_post = new visual.Polygon ({
    win: psychoJS.window, name: 'choice_9_post', 
    edges: 100, size:[0.03, 0.03],
    ori: 0, pos: [0.3, (- 0.18)],
    lineWidth: 1, lineColor: new util.Color([(- 0.9), (- 0.9), (- 0.9)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -9, interpolate: true,
  });
  
  select_answer_mouse_3 = new core.Mouse({
    win: psychoJS.window,
  });
  select_answer_mouse_3.mouseClock = new util.Clock();
  // Initialize components for Routine "highlight_post_sam_hu"
  highlight_post_sam_huClock = new util.Clock();
  sam_hu_highlight_post = new visual.ImageStim({
    win : psychoJS.window,
    name : 'sam_hu_highlight_post', units : undefined, 
    image : 'SAM/SAM_hu.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [1, 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "SAM_ec_directions"
  SAM_ec_directionsClock = new util.Clock();
  SAM_ec_instructions = new visual.ImageStim({
    win : psychoJS.window,
    name : 'SAM_ec_instructions', units : undefined, 
    image : 'SAM/SAM_ec_ins.jpg', mask : undefined,
    ori : 0, pos : [0, 0], size : [1, 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  SAM_ec_instructions_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SAM_ec_question_2"
  SAM_ec_question_2Clock = new util.Clock();
  SAM_ec_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'SAM_ec_2', units : undefined, 
    image : 'SAM/SAM_ec.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [1, 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  choice_num_1_post = new visual.Polygon ({
    win: psychoJS.window, name: 'choice_num_1_post', 
    edges: 100, size:[0.03, 0.03],
    ori: 0, pos: [(- 0.3), (- 0.18)],
    lineWidth: 1, lineColor: new util.Color([(- 0.9), (- 0.9), (- 0.9)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  choice_num_2_post = new visual.Polygon ({
    win: psychoJS.window, name: 'choice_num_2_post', 
    edges: 100, size:[0.03, 0.03],
    ori: 0, pos: [(- 0.22), (- 0.18)],
    lineWidth: 1, lineColor: new util.Color([(- 0.9), (- 0.9), (- 0.9)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  choice_num_3_post = new visual.Polygon ({
    win: psychoJS.window, name: 'choice_num_3_post', 
    edges: 100, size:[0.03, 0.03],
    ori: 0, pos: [(- 0.15), (- 0.18)],
    lineWidth: 1, lineColor: new util.Color([(- 0.9), (- 0.9), (- 0.9)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  choice_num_4_post = new visual.Polygon ({
    win: psychoJS.window, name: 'choice_num_4_post', 
    edges: 100, size:[0.03, 0.03],
    ori: 0, pos: [(- 0.07), (- 0.18)],
    lineWidth: 1, lineColor: new util.Color([(- 0.9), (- 0.9), (- 0.9)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -4, interpolate: true,
  });
  
  choice_num_5_post = new visual.Polygon ({
    win: psychoJS.window, name: 'choice_num_5_post', 
    edges: 100, size:[0.03, 0.03],
    ori: 0, pos: [0, (- 0.18)],
    lineWidth: 1, lineColor: new util.Color([(- 0.9), (- 0.9), (- 0.9)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -5, interpolate: true,
  });
  
  choice_num_6_post = new visual.Polygon ({
    win: psychoJS.window, name: 'choice_num_6_post', 
    edges: 100, size:[0.03, 0.03],
    ori: 0, pos: [0.07, (- 0.18)],
    lineWidth: 1, lineColor: new util.Color([(- 0.9), (- 0.9), (- 0.9)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -6, interpolate: true,
  });
  
  choice_num_7_post = new visual.Polygon ({
    win: psychoJS.window, name: 'choice_num_7_post', 
    edges: 100, size:[0.03, 0.03],
    ori: 0, pos: [0.15, (- 0.18)],
    lineWidth: 1, lineColor: new util.Color([(- 0.9), (- 0.9), (- 0.9)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -7, interpolate: true,
  });
  
  choice_num_8_post = new visual.Polygon ({
    win: psychoJS.window, name: 'choice_num_8_post', 
    edges: 100, size:[0.03, 0.03],
    ori: 0, pos: [0.22, (- 0.18)],
    lineWidth: 1, lineColor: new util.Color([(- 0.9), (- 0.9), (- 0.9)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -8, interpolate: true,
  });
  
  choice_num_9_post = new visual.Polygon ({
    win: psychoJS.window, name: 'choice_num_9_post', 
    edges: 100, size:[0.03, 0.03],
    ori: 0, pos: [0.3, (- 0.18)],
    lineWidth: 1, lineColor: new util.Color([(- 0.9), (- 0.9), (- 0.9)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -9, interpolate: true,
  });
  
  select_answer_mouse_4 = new core.Mouse({
    win: psychoJS.window,
  });
  select_answer_mouse_4.mouseClock = new util.Clock();
  // Initialize components for Routine "highlight_sam_ec_post_choice"
  highlight_sam_ec_post_choiceClock = new util.Clock();
  sam_ec_post_highlight = new visual.ImageStim({
    win : psychoJS.window,
    name : 'sam_ec_post_highlight', units : undefined, 
    image : 'SAM/SAM_ec.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [1, 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "total_points_end_experiment"
  total_points_end_experimentClock = new util.Clock();
  final_total_points = new visual.TextStim({
    win: psychoJS.window,
    name: 'final_total_points',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.07), 0.03], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  rest_of_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'rest_of_text',
    text: 'You have earned         out of a possible 160 points.\n\nPlease click any button to exit.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.01)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  exit_task = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var initialize_stim_and_key_variablesComponents;
function initialize_stim_and_key_variablesRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'initialize_stim_and_key_variables'-------
    t = 0;
    initialize_stim_and_key_variablesClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // keep track of which components have finished
    initialize_stim_and_key_variablesComponents = [];
    
    for (const thisComponent of initialize_stim_and_key_variablesComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var continueRoutine;
function initialize_stim_and_key_variablesRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'initialize_stim_and_key_variables'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = initialize_stim_and_key_variablesClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of initialize_stim_and_key_variablesComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function initialize_stim_and_key_variablesRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'initialize_stim_and_key_variables'-------
    for (const thisComponent of initialize_stim_and_key_variablesComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "initialize_stim_and_key_variables" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _enter_email_allKeys;
var get_emailComponents;
function get_emailRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'get_email'-------
    t = 0;
    get_emailClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    textbox_email.setText('Type email here');
    enter_email.keys = undefined;
    enter_email.rt = undefined;
    _enter_email_allKeys = [];
    // keep track of which components have finished
    get_emailComponents = [];
    get_emailComponents.push(email_instructions);
    get_emailComponents.push(textbox_email);
    get_emailComponents.push(enter_email);
    get_emailComponents.push(submit_text);
    
    for (const thisComponent of get_emailComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function get_emailRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'get_email'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = get_emailClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *email_instructions* updates
    if (t >= 0.0 && email_instructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      email_instructions.tStart = t;  // (not accounting for frame time here)
      email_instructions.frameNStart = frameN;  // exact frame index
      
      email_instructions.setAutoDraw(true);
    }

    
    // *textbox_email* updates
    if (t >= 0.0 && textbox_email.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textbox_email.tStart = t;  // (not accounting for frame time here)
      textbox_email.frameNStart = frameN;  // exact frame index
      
      textbox_email.setAutoDraw(true);
    }

    
    if (textbox_email.status === PsychoJS.Status.STARTED){ // only update if being drawn
      textbox_email.setPadding();
    }
    
    // *enter_email* updates
    if (t >= 0.0 && enter_email.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enter_email.tStart = t;  // (not accounting for frame time here)
      enter_email.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { enter_email.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { enter_email.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { enter_email.clearEvents(); });
    }

    if (enter_email.status === PsychoJS.Status.STARTED) {
      let theseKeys = enter_email.getKeys({keyList: ['enter', 'return'], waitRelease: false});
      _enter_email_allKeys = _enter_email_allKeys.concat(theseKeys);
      if (_enter_email_allKeys.length > 0) {
        enter_email.keys = _enter_email_allKeys[_enter_email_allKeys.length - 1].name;  // just the last key pressed
        enter_email.rt = _enter_email_allKeys[_enter_email_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *submit_text* updates
    if (t >= 0.0 && submit_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      submit_text.tStart = t;  // (not accounting for frame time here)
      submit_text.frameNStart = frameN;  // exact frame index
      
      submit_text.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of get_emailComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var thisExp;
function get_emailRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'get_email'-------
    for (const thisComponent of get_emailComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('textbox_email.text', textbox_email.text);
    psychoJS.experiment.addData('enter_email.keys', enter_email.keys);
    if (typeof enter_email.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('enter_email.rt', enter_email.rt);
        routineTimer.reset();
        }
    
    enter_email.stop();
    thisExp = psychoJS.experiment;
    thisExp.addData("email", textbox_email._pixi.text);
    
    // the Routine "get_email" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _welcome_slide_key_resp_allKeys;
var welcome_slideComponents;
function welcome_slideRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'welcome_slide'-------
    t = 0;
    welcome_slideClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    welcome_slide_key_resp.keys = undefined;
    welcome_slide_key_resp.rt = undefined;
    _welcome_slide_key_resp_allKeys = [];
    // keep track of which components have finished
    welcome_slideComponents = [];
    welcome_slideComponents.push(slide_1_inst);
    welcome_slideComponents.push(welcome_slide_key_resp);
    
    for (const thisComponent of welcome_slideComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function welcome_slideRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'welcome_slide'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = welcome_slideClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *slide_1_inst* updates
    if (t >= 0.0 && slide_1_inst.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slide_1_inst.tStart = t;  // (not accounting for frame time here)
      slide_1_inst.frameNStart = frameN;  // exact frame index
      
      slide_1_inst.setAutoDraw(true);
    }

    
    // *welcome_slide_key_resp* updates
    if (t >= 0.0 && welcome_slide_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcome_slide_key_resp.tStart = t;  // (not accounting for frame time here)
      welcome_slide_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { welcome_slide_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { welcome_slide_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { welcome_slide_key_resp.clearEvents(); });
    }

    if (welcome_slide_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = welcome_slide_key_resp.getKeys({keyList: [], waitRelease: false});
      _welcome_slide_key_resp_allKeys = _welcome_slide_key_resp_allKeys.concat(theseKeys);
      if (_welcome_slide_key_resp_allKeys.length > 0) {
        welcome_slide_key_resp.keys = _welcome_slide_key_resp_allKeys[_welcome_slide_key_resp_allKeys.length - 1].name;  // just the last key pressed
        welcome_slide_key_resp.rt = _welcome_slide_key_resp_allKeys[_welcome_slide_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of welcome_slideComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function welcome_slideRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'welcome_slide'-------
    for (const thisComponent of welcome_slideComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('welcome_slide_key_resp.keys', welcome_slide_key_resp.keys);
    if (typeof welcome_slide_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('welcome_slide_key_resp.rt', welcome_slide_key_resp.rt);
        routineTimer.reset();
        }
    
    welcome_slide_key_resp.stop();
    // the Routine "welcome_slide" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _SAM_hu_instructions_key_resp_allKeys;
var SAM_hu_directionsComponents;
function SAM_hu_directionsRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'SAM_hu_directions'-------
    t = 0;
    SAM_hu_directionsClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    SAM_hu_instructions_key_resp.keys = undefined;
    SAM_hu_instructions_key_resp.rt = undefined;
    _SAM_hu_instructions_key_resp_allKeys = [];
    // keep track of which components have finished
    SAM_hu_directionsComponents = [];
    SAM_hu_directionsComponents.push(SAM_hu_instructions);
    SAM_hu_directionsComponents.push(SAM_hu_instructions_key_resp);
    
    for (const thisComponent of SAM_hu_directionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function SAM_hu_directionsRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'SAM_hu_directions'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = SAM_hu_directionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *SAM_hu_instructions* updates
    if (t >= 0.0 && SAM_hu_instructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SAM_hu_instructions.tStart = t;  // (not accounting for frame time here)
      SAM_hu_instructions.frameNStart = frameN;  // exact frame index
      
      SAM_hu_instructions.setAutoDraw(true);
    }

    
    // *SAM_hu_instructions_key_resp* updates
    if (t >= 0.0 && SAM_hu_instructions_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SAM_hu_instructions_key_resp.tStart = t;  // (not accounting for frame time here)
      SAM_hu_instructions_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { SAM_hu_instructions_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { SAM_hu_instructions_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { SAM_hu_instructions_key_resp.clearEvents(); });
    }

    if (SAM_hu_instructions_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = SAM_hu_instructions_key_resp.getKeys({keyList: [], waitRelease: false});
      _SAM_hu_instructions_key_resp_allKeys = _SAM_hu_instructions_key_resp_allKeys.concat(theseKeys);
      if (_SAM_hu_instructions_key_resp_allKeys.length > 0) {
        SAM_hu_instructions_key_resp.keys = _SAM_hu_instructions_key_resp_allKeys[_SAM_hu_instructions_key_resp_allKeys.length - 1].name;  // just the last key pressed
        SAM_hu_instructions_key_resp.rt = _SAM_hu_instructions_key_resp_allKeys[_SAM_hu_instructions_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of SAM_hu_directionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SAM_hu_directionsRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'SAM_hu_directions'-------
    for (const thisComponent of SAM_hu_directionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('SAM_hu_instructions_key_resp.keys', SAM_hu_instructions_key_resp.keys);
    if (typeof SAM_hu_instructions_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('SAM_hu_instructions_key_resp.rt', SAM_hu_instructions_key_resp.rt);
        routineTimer.reset();
        }
    
    SAM_hu_instructions_key_resp.stop();
    // the Routine "SAM_hu_directions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var gotValidClick;
var SAM_hu_questionComponents;
function SAM_hu_questionRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'SAM_hu_question'-------
    t = 0;
    SAM_hu_questionClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // setup some python lists for storing info about the select_answer_mouse_sam_hu
    select_answer_mouse_sam_hu.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    SAM_hu_questionComponents = [];
    SAM_hu_questionComponents.push(SAM_hu);
    SAM_hu_questionComponents.push(choice_1);
    SAM_hu_questionComponents.push(choice_2);
    SAM_hu_questionComponents.push(choice_3);
    SAM_hu_questionComponents.push(choice_4);
    SAM_hu_questionComponents.push(choice_5);
    SAM_hu_questionComponents.push(choice_6);
    SAM_hu_questionComponents.push(choice_7);
    SAM_hu_questionComponents.push(choice_8);
    SAM_hu_questionComponents.push(choice_9);
    SAM_hu_questionComponents.push(select_answer_mouse_sam_hu);
    
    for (const thisComponent of SAM_hu_questionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var prevButtonState;
var _mouseButtons;
function SAM_hu_questionRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'SAM_hu_question'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = SAM_hu_questionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *SAM_hu* updates
    if (t >= 0.0 && SAM_hu.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SAM_hu.tStart = t;  // (not accounting for frame time here)
      SAM_hu.frameNStart = frameN;  // exact frame index
      
      SAM_hu.setAutoDraw(true);
    }

    
    // *choice_1* updates
    if (t >= 0.0 && choice_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_1.tStart = t;  // (not accounting for frame time here)
      choice_1.frameNStart = frameN;  // exact frame index
      
      choice_1.setAutoDraw(true);
    }

    
    // *choice_2* updates
    if (t >= 0.0 && choice_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_2.tStart = t;  // (not accounting for frame time here)
      choice_2.frameNStart = frameN;  // exact frame index
      
      choice_2.setAutoDraw(true);
    }

    
    // *choice_3* updates
    if (t >= 0.0 && choice_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_3.tStart = t;  // (not accounting for frame time here)
      choice_3.frameNStart = frameN;  // exact frame index
      
      choice_3.setAutoDraw(true);
    }

    
    // *choice_4* updates
    if (t >= 0.0 && choice_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_4.tStart = t;  // (not accounting for frame time here)
      choice_4.frameNStart = frameN;  // exact frame index
      
      choice_4.setAutoDraw(true);
    }

    
    // *choice_5* updates
    if (t >= 0.0 && choice_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_5.tStart = t;  // (not accounting for frame time here)
      choice_5.frameNStart = frameN;  // exact frame index
      
      choice_5.setAutoDraw(true);
    }

    
    // *choice_6* updates
    if (t >= 0.0 && choice_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_6.tStart = t;  // (not accounting for frame time here)
      choice_6.frameNStart = frameN;  // exact frame index
      
      choice_6.setAutoDraw(true);
    }

    
    // *choice_7* updates
    if (t >= 0.0 && choice_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_7.tStart = t;  // (not accounting for frame time here)
      choice_7.frameNStart = frameN;  // exact frame index
      
      choice_7.setAutoDraw(true);
    }

    
    // *choice_8* updates
    if (t >= 0.0 && choice_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_8.tStart = t;  // (not accounting for frame time here)
      choice_8.frameNStart = frameN;  // exact frame index
      
      choice_8.setAutoDraw(true);
    }

    
    // *choice_9* updates
    if (t >= 0.0 && choice_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_9.tStart = t;  // (not accounting for frame time here)
      choice_9.frameNStart = frameN;  // exact frame index
      
      choice_9.setAutoDraw(true);
    }

    // *select_answer_mouse_sam_hu* updates
    if (t >= 0.0 && select_answer_mouse_sam_hu.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      select_answer_mouse_sam_hu.tStart = t;  // (not accounting for frame time here)
      select_answer_mouse_sam_hu.frameNStart = frameN;  // exact frame index
      
      select_answer_mouse_sam_hu.status = PsychoJS.Status.STARTED;
      select_answer_mouse_sam_hu.mouseClock.reset();
      prevButtonState = select_answer_mouse_sam_hu.getPressed();  // if button is down already this ISN'T a new click
      }
    if (select_answer_mouse_sam_hu.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = select_answer_mouse_sam_hu.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [choice_1,choice_2,choice_3,choice_4,choice_5,choice_6,choice_7,choice_8,choice_9]) {
            if (obj.contains(select_answer_mouse_sam_hu)) {
              gotValidClick = true;
              select_answer_mouse_sam_hu.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of SAM_hu_questionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var _mouseXYs;
var answer_to_draw;
function SAM_hu_questionRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'SAM_hu_question'-------
    for (const thisComponent of SAM_hu_questionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for thisExp (ExperimentHandler)
    _mouseXYs = select_answer_mouse_sam_hu.getPos();
    _mouseButtons = select_answer_mouse_sam_hu.getPressed();
    psychoJS.experiment.addData('select_answer_mouse_sam_hu.x', _mouseXYs[0]);
    psychoJS.experiment.addData('select_answer_mouse_sam_hu.y', _mouseXYs[1]);
    psychoJS.experiment.addData('select_answer_mouse_sam_hu.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('select_answer_mouse_sam_hu.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('select_answer_mouse_sam_hu.rightButton', _mouseButtons[2]);
    if (select_answer_mouse_sam_hu.clicked_name.length > 0) {
      psychoJS.experiment.addData('select_answer_mouse_sam_hu.clicked_name', select_answer_mouse_sam_hu.clicked_name[0]);}
    answer_to_draw = [];
    for (var answer, _pj_c = 0, _pj_a = [choice_1, choice_2, choice_3, choice_4, choice_5, choice_6, choice_7, choice_8, choice_9], _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        answer = _pj_a[_pj_c];
        if (select_answer_mouse_sam_hu.isPressedIn(answer)) {
            answer_to_draw = answer;
        }
    }
    
    // the Routine "SAM_hu_question" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var highlight_sam_hu_pre_choiceComponents;
function highlight_sam_hu_pre_choiceRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'highlight_sam_hu_pre_choice'-------
    t = 0;
    highlight_sam_hu_pre_choiceClock.reset(); // clock
    frameN = -1;
    routineTimer.add(0.300000);
    // update component parameters for each repeat
    // keep track of which components have finished
    highlight_sam_hu_pre_choiceComponents = [];
    highlight_sam_hu_pre_choiceComponents.push(Sam_hu_highlight_pre);
    
    for (const thisComponent of highlight_sam_hu_pre_choiceComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var frameRemains;
function highlight_sam_hu_pre_choiceRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'highlight_sam_hu_pre_choice'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = highlight_sam_hu_pre_choiceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Sam_hu_highlight_pre* updates
    if (t >= 0.0 && Sam_hu_highlight_pre.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Sam_hu_highlight_pre.tStart = t;  // (not accounting for frame time here)
      Sam_hu_highlight_pre.frameNStart = frameN;  // exact frame index
      
      Sam_hu_highlight_pre.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Sam_hu_highlight_pre.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Sam_hu_highlight_pre.setAutoDraw(false);
    }
    answer_to_draw.fillColor = [0.3, 0.5, 0.7];
    answer_to_draw.setAutoDraw(true);
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of highlight_sam_hu_pre_choiceComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function highlight_sam_hu_pre_choiceRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'highlight_sam_hu_pre_choice'-------
    for (const thisComponent of highlight_sam_hu_pre_choiceComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    answer_to_draw.setAutoDraw(false);
    
    return Scheduler.Event.NEXT;
  };
}


var _SAM_ec_instructions_key_resp_allKeys;
var SAM_ec_directionsComponents;
function SAM_ec_directionsRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'SAM_ec_directions'-------
    t = 0;
    SAM_ec_directionsClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    SAM_ec_instructions_key_resp.keys = undefined;
    SAM_ec_instructions_key_resp.rt = undefined;
    _SAM_ec_instructions_key_resp_allKeys = [];
    // keep track of which components have finished
    SAM_ec_directionsComponents = [];
    SAM_ec_directionsComponents.push(SAM_ec_instructions);
    SAM_ec_directionsComponents.push(SAM_ec_instructions_key_resp);
    
    for (const thisComponent of SAM_ec_directionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function SAM_ec_directionsRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'SAM_ec_directions'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = SAM_ec_directionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *SAM_ec_instructions* updates
    if (t >= 0.0 && SAM_ec_instructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SAM_ec_instructions.tStart = t;  // (not accounting for frame time here)
      SAM_ec_instructions.frameNStart = frameN;  // exact frame index
      
      SAM_ec_instructions.setAutoDraw(true);
    }

    
    // *SAM_ec_instructions_key_resp* updates
    if (t >= 0.0 && SAM_ec_instructions_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SAM_ec_instructions_key_resp.tStart = t;  // (not accounting for frame time here)
      SAM_ec_instructions_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { SAM_ec_instructions_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { SAM_ec_instructions_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { SAM_ec_instructions_key_resp.clearEvents(); });
    }

    if (SAM_ec_instructions_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = SAM_ec_instructions_key_resp.getKeys({keyList: [], waitRelease: false});
      _SAM_ec_instructions_key_resp_allKeys = _SAM_ec_instructions_key_resp_allKeys.concat(theseKeys);
      if (_SAM_ec_instructions_key_resp_allKeys.length > 0) {
        SAM_ec_instructions_key_resp.keys = _SAM_ec_instructions_key_resp_allKeys[_SAM_ec_instructions_key_resp_allKeys.length - 1].name;  // just the last key pressed
        SAM_ec_instructions_key_resp.rt = _SAM_ec_instructions_key_resp_allKeys[_SAM_ec_instructions_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of SAM_ec_directionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SAM_ec_directionsRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'SAM_ec_directions'-------
    for (const thisComponent of SAM_ec_directionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('SAM_ec_instructions_key_resp.keys', SAM_ec_instructions_key_resp.keys);
    if (typeof SAM_ec_instructions_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('SAM_ec_instructions_key_resp.rt', SAM_ec_instructions_key_resp.rt);
        routineTimer.reset();
        }
    
    SAM_ec_instructions_key_resp.stop();
    // the Routine "SAM_ec_directions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var SAM_ec_questionComponents;
function SAM_ec_questionRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'SAM_ec_question'-------
    t = 0;
    SAM_ec_questionClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // setup some python lists for storing info about the select_answer_mouse_sam_ec
    select_answer_mouse_sam_ec.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    SAM_ec_questionComponents = [];
    SAM_ec_questionComponents.push(SAM_ec);
    SAM_ec_questionComponents.push(choice_num_1);
    SAM_ec_questionComponents.push(choice_num_2);
    SAM_ec_questionComponents.push(choice_num_3);
    SAM_ec_questionComponents.push(choice_num_4);
    SAM_ec_questionComponents.push(choice_num_5);
    SAM_ec_questionComponents.push(choice_num_6);
    SAM_ec_questionComponents.push(choice_num_7);
    SAM_ec_questionComponents.push(choice_num_8);
    SAM_ec_questionComponents.push(choice_num_9);
    SAM_ec_questionComponents.push(select_answer_mouse_sam_ec);
    
    for (const thisComponent of SAM_ec_questionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function SAM_ec_questionRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'SAM_ec_question'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = SAM_ec_questionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *SAM_ec* updates
    if (t >= 0.0 && SAM_ec.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SAM_ec.tStart = t;  // (not accounting for frame time here)
      SAM_ec.frameNStart = frameN;  // exact frame index
      
      SAM_ec.setAutoDraw(true);
    }

    
    // *choice_num_1* updates
    if (t >= 0.0 && choice_num_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_num_1.tStart = t;  // (not accounting for frame time here)
      choice_num_1.frameNStart = frameN;  // exact frame index
      
      choice_num_1.setAutoDraw(true);
    }

    
    // *choice_num_2* updates
    if (t >= 0.0 && choice_num_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_num_2.tStart = t;  // (not accounting for frame time here)
      choice_num_2.frameNStart = frameN;  // exact frame index
      
      choice_num_2.setAutoDraw(true);
    }

    
    // *choice_num_3* updates
    if (t >= 0.0 && choice_num_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_num_3.tStart = t;  // (not accounting for frame time here)
      choice_num_3.frameNStart = frameN;  // exact frame index
      
      choice_num_3.setAutoDraw(true);
    }

    
    // *choice_num_4* updates
    if (t >= 0.0 && choice_num_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_num_4.tStart = t;  // (not accounting for frame time here)
      choice_num_4.frameNStart = frameN;  // exact frame index
      
      choice_num_4.setAutoDraw(true);
    }

    
    // *choice_num_5* updates
    if (t >= 0.0 && choice_num_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_num_5.tStart = t;  // (not accounting for frame time here)
      choice_num_5.frameNStart = frameN;  // exact frame index
      
      choice_num_5.setAutoDraw(true);
    }

    
    // *choice_num_6* updates
    if (t >= 0.0 && choice_num_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_num_6.tStart = t;  // (not accounting for frame time here)
      choice_num_6.frameNStart = frameN;  // exact frame index
      
      choice_num_6.setAutoDraw(true);
    }

    
    // *choice_num_7* updates
    if (t >= 0.0 && choice_num_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_num_7.tStart = t;  // (not accounting for frame time here)
      choice_num_7.frameNStart = frameN;  // exact frame index
      
      choice_num_7.setAutoDraw(true);
    }

    
    // *choice_num_8* updates
    if (t >= 0.0 && choice_num_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_num_8.tStart = t;  // (not accounting for frame time here)
      choice_num_8.frameNStart = frameN;  // exact frame index
      
      choice_num_8.setAutoDraw(true);
    }

    
    // *choice_num_9* updates
    if (t >= 0.0 && choice_num_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_num_9.tStart = t;  // (not accounting for frame time here)
      choice_num_9.frameNStart = frameN;  // exact frame index
      
      choice_num_9.setAutoDraw(true);
    }

    // *select_answer_mouse_sam_ec* updates
    if (t >= 0.0 && select_answer_mouse_sam_ec.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      select_answer_mouse_sam_ec.tStart = t;  // (not accounting for frame time here)
      select_answer_mouse_sam_ec.frameNStart = frameN;  // exact frame index
      
      select_answer_mouse_sam_ec.status = PsychoJS.Status.STARTED;
      select_answer_mouse_sam_ec.mouseClock.reset();
      prevButtonState = select_answer_mouse_sam_ec.getPressed();  // if button is down already this ISN'T a new click
      }
    if (select_answer_mouse_sam_ec.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = select_answer_mouse_sam_ec.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [choice_num_1,choice_num_2,choice_num_3,choice_num_4,choice_num_5,choice_num_6,choice_num_7,choice_num_8,choice_num_9]) {
            if (obj.contains(select_answer_mouse_sam_ec)) {
              gotValidClick = true;
              select_answer_mouse_sam_ec.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of SAM_ec_questionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SAM_ec_questionRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'SAM_ec_question'-------
    for (const thisComponent of SAM_ec_questionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for thisExp (ExperimentHandler)
    _mouseXYs = select_answer_mouse_sam_ec.getPos();
    _mouseButtons = select_answer_mouse_sam_ec.getPressed();
    psychoJS.experiment.addData('select_answer_mouse_sam_ec.x', _mouseXYs[0]);
    psychoJS.experiment.addData('select_answer_mouse_sam_ec.y', _mouseXYs[1]);
    psychoJS.experiment.addData('select_answer_mouse_sam_ec.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('select_answer_mouse_sam_ec.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('select_answer_mouse_sam_ec.rightButton', _mouseButtons[2]);
    if (select_answer_mouse_sam_ec.clicked_name.length > 0) {
      psychoJS.experiment.addData('select_answer_mouse_sam_ec.clicked_name', select_answer_mouse_sam_ec.clicked_name[0]);}
    answer_to_draw = [];
    for (var answer, _pj_c = 0, _pj_a = [choice_num_1, choice_num_2, choice_num_3, choice_num_4, choice_num_5, choice_num_6, choice_num_7, choice_num_8, choice_num_9], _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        answer = _pj_a[_pj_c];
        if (select_answer_mouse_sam_ec.isPressedIn(answer)) {
            answer_to_draw = answer;
        }
    }
    
    // the Routine "SAM_ec_question" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var highlight_sam_ec_pre_choiceComponents;
function highlight_sam_ec_pre_choiceRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'highlight_sam_ec_pre_choice'-------
    t = 0;
    highlight_sam_ec_pre_choiceClock.reset(); // clock
    frameN = -1;
    routineTimer.add(0.300000);
    // update component parameters for each repeat
    // keep track of which components have finished
    highlight_sam_ec_pre_choiceComponents = [];
    highlight_sam_ec_pre_choiceComponents.push(sam_ec_pre_highlight);
    
    for (const thisComponent of highlight_sam_ec_pre_choiceComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function highlight_sam_ec_pre_choiceRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'highlight_sam_ec_pre_choice'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = highlight_sam_ec_pre_choiceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *sam_ec_pre_highlight* updates
    if (t >= 0.0 && sam_ec_pre_highlight.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sam_ec_pre_highlight.tStart = t;  // (not accounting for frame time here)
      sam_ec_pre_highlight.frameNStart = frameN;  // exact frame index
      
      sam_ec_pre_highlight.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (sam_ec_pre_highlight.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      sam_ec_pre_highlight.setAutoDraw(false);
    }
    answer_to_draw.fillColor = [0.3, 0.5, 0.7];
    answer_to_draw.setAutoDraw(true);
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of highlight_sam_ec_pre_choiceComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function highlight_sam_ec_pre_choiceRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'highlight_sam_ec_pre_choice'-------
    for (const thisComponent of highlight_sam_ec_pre_choiceComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    answer_to_draw.setAutoDraw(false);
    
    return Scheduler.Event.NEXT;
  };
}


var _draw_kb_key_resp_allKeys;
var introduce_keyboard_hand_positioningComponents;
function introduce_keyboard_hand_positioningRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'introduce_keyboard_hand_positioning'-------
    t = 0;
    introduce_keyboard_hand_positioningClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    intro_to_kb.setAutoDraw(true);
    
    draw_kb_key_resp.keys = undefined;
    draw_kb_key_resp.rt = undefined;
    _draw_kb_key_resp_allKeys = [];
    // keep track of which components have finished
    introduce_keyboard_hand_positioningComponents = [];
    introduce_keyboard_hand_positioningComponents.push(draw_kb_key_resp);
    
    for (const thisComponent of introduce_keyboard_hand_positioningComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function introduce_keyboard_hand_positioningRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'introduce_keyboard_hand_positioning'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = introduce_keyboard_hand_positioningClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *draw_kb_key_resp* updates
    if (t >= 0.0 && draw_kb_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      draw_kb_key_resp.tStart = t;  // (not accounting for frame time here)
      draw_kb_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { draw_kb_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { draw_kb_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { draw_kb_key_resp.clearEvents(); });
    }

    if (draw_kb_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = draw_kb_key_resp.getKeys({keyList: [], waitRelease: false});
      _draw_kb_key_resp_allKeys = _draw_kb_key_resp_allKeys.concat(theseKeys);
      if (_draw_kb_key_resp_allKeys.length > 0) {
        draw_kb_key_resp.keys = _draw_kb_key_resp_allKeys[_draw_kb_key_resp_allKeys.length - 1].name;  // just the last key pressed
        draw_kb_key_resp.rt = _draw_kb_key_resp_allKeys[_draw_kb_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of introduce_keyboard_hand_positioningComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function introduce_keyboard_hand_positioningRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'introduce_keyboard_hand_positioning'-------
    for (const thisComponent of introduce_keyboard_hand_positioningComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    intro_to_kb.setAutoDraw(false);
    
    psychoJS.experiment.addData('draw_kb_key_resp.keys', draw_kb_key_resp.keys);
    if (typeof draw_kb_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('draw_kb_key_resp.rt', draw_kb_key_resp.rt);
        routineTimer.reset();
        }
    
    draw_kb_key_resp.stop();
    // the Routine "introduce_keyboard_hand_positioning" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _begin_task_instructions_key_resp_allKeys;
var begin_instructionsComponents;
function begin_instructionsRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'begin_instructions'-------
    t = 0;
    begin_instructionsClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    if ((instruction_slide_2_selection === 1)) {
        fractal_blossom.pos = [(- 0.12), 0.13];
        fractal_octopus.pos = [0.12, 0.13];
        instructions_slide_two.setAutoDraw(true);
        fractal_blossom.setAutoDraw(true);
        fractal_octopus.setAutoDraw(true);
    } else {
        if ((instruction_slide_2_selection === 2)) {
            fractal_blossom.pos = [0.12, 0.13];
            fractal_octopus.pos = [(- 0.12), 0.13];
            instructions_slide_two.setAutoDraw(true);
            fractal_blossom.setAutoDraw(true);
            fractal_octopus.setAutoDraw(true);
        }
    }
    
    begin_task_instructions_key_resp.keys = undefined;
    begin_task_instructions_key_resp.rt = undefined;
    _begin_task_instructions_key_resp_allKeys = [];
    // keep track of which components have finished
    begin_instructionsComponents = [];
    begin_instructionsComponents.push(begin_task_instructions_key_resp);
    
    for (const thisComponent of begin_instructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function begin_instructionsRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'begin_instructions'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = begin_instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *begin_task_instructions_key_resp* updates
    if (t >= 0.0 && begin_task_instructions_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      begin_task_instructions_key_resp.tStart = t;  // (not accounting for frame time here)
      begin_task_instructions_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { begin_task_instructions_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { begin_task_instructions_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { begin_task_instructions_key_resp.clearEvents(); });
    }

    if (begin_task_instructions_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = begin_task_instructions_key_resp.getKeys({keyList: [], waitRelease: false});
      _begin_task_instructions_key_resp_allKeys = _begin_task_instructions_key_resp_allKeys.concat(theseKeys);
      if (_begin_task_instructions_key_resp_allKeys.length > 0) {
        begin_task_instructions_key_resp.keys = _begin_task_instructions_key_resp_allKeys[_begin_task_instructions_key_resp_allKeys.length - 1].name;  // just the last key pressed
        begin_task_instructions_key_resp.rt = _begin_task_instructions_key_resp_allKeys[_begin_task_instructions_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of begin_instructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function begin_instructionsRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'begin_instructions'-------
    for (const thisComponent of begin_instructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    if ((instruction_slide_2_selection === 1)) {
        fractal_blossom.pos = [(- 0.12), 0.13];
        fractal_octopus.pos = [0.12, 0.13];
        instructions_slide_two.setAutoDraw(false);
        fractal_blossom.setAutoDraw(false);
        fractal_octopus.setAutoDraw(false);
    } else {
        if ((instruction_slide_2_selection === 2)) {
            fractal_blossom.pos = [0.12, 0.13];
            fractal_octopus.pos = [(- 0.12), 0.13];
            instructions_slide_two.setAutoDraw(false);
            fractal_blossom.setAutoDraw(false);
            fractal_octopus.setAutoDraw(false);
        }
    }
    
    psychoJS.experiment.addData('begin_task_instructions_key_resp.keys', begin_task_instructions_key_resp.keys);
    if (typeof begin_task_instructions_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('begin_task_instructions_key_resp.rt', begin_task_instructions_key_resp.rt);
        routineTimer.reset();
        }
    
    begin_task_instructions_key_resp.stop();
    // the Routine "begin_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _slide_two_key_response_allKeys;
var continue_beginComponents;
function continue_beginRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'continue_begin'-------
    t = 0;
    continue_beginClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    instructions_slide_two_second.setAutoDraw(true);
    
    slide_two_key_response.keys = undefined;
    slide_two_key_response.rt = undefined;
    _slide_two_key_response_allKeys = [];
    // keep track of which components have finished
    continue_beginComponents = [];
    continue_beginComponents.push(slide_two_key_response);
    
    for (const thisComponent of continue_beginComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function continue_beginRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'continue_begin'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = continue_beginClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *slide_two_key_response* updates
    if (t >= 0.0 && slide_two_key_response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slide_two_key_response.tStart = t;  // (not accounting for frame time here)
      slide_two_key_response.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { slide_two_key_response.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { slide_two_key_response.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { slide_two_key_response.clearEvents(); });
    }

    if (slide_two_key_response.status === PsychoJS.Status.STARTED) {
      let theseKeys = slide_two_key_response.getKeys({keyList: [], waitRelease: false});
      _slide_two_key_response_allKeys = _slide_two_key_response_allKeys.concat(theseKeys);
      if (_slide_two_key_response_allKeys.length > 0) {
        slide_two_key_response.keys = _slide_two_key_response_allKeys[_slide_two_key_response_allKeys.length - 1].name;  // just the last key pressed
        slide_two_key_response.rt = _slide_two_key_response_allKeys[_slide_two_key_response_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of continue_beginComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function continue_beginRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'continue_begin'-------
    for (const thisComponent of continue_beginComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    instructions_slide_two_second.setAutoDraw(false);
    
    psychoJS.experiment.addData('slide_two_key_response.keys', slide_two_key_response.keys);
    if (typeof slide_two_key_response.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('slide_two_key_response.rt', slide_two_key_response.rt);
        routineTimer.reset();
        }
    
    slide_two_key_response.stop();
    // the Routine "continue_begin" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _max_points_slide_key_resp_allKeys;
var slide_max_pointsComponents;
function slide_max_pointsRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'slide_max_points'-------
    t = 0;
    slide_max_pointsClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    max_points.setAutoDraw(true);
    
    max_points_slide_key_resp.keys = undefined;
    max_points_slide_key_resp.rt = undefined;
    _max_points_slide_key_resp_allKeys = [];
    // keep track of which components have finished
    slide_max_pointsComponents = [];
    slide_max_pointsComponents.push(max_points_slide_key_resp);
    
    for (const thisComponent of slide_max_pointsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function slide_max_pointsRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'slide_max_points'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = slide_max_pointsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *max_points_slide_key_resp* updates
    if (t >= 0.0 && max_points_slide_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      max_points_slide_key_resp.tStart = t;  // (not accounting for frame time here)
      max_points_slide_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { max_points_slide_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { max_points_slide_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { max_points_slide_key_resp.clearEvents(); });
    }

    if (max_points_slide_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = max_points_slide_key_resp.getKeys({keyList: [], waitRelease: false});
      _max_points_slide_key_resp_allKeys = _max_points_slide_key_resp_allKeys.concat(theseKeys);
      if (_max_points_slide_key_resp_allKeys.length > 0) {
        max_points_slide_key_resp.keys = _max_points_slide_key_resp_allKeys[_max_points_slide_key_resp_allKeys.length - 1].name;  // just the last key pressed
        max_points_slide_key_resp.rt = _max_points_slide_key_resp_allKeys[_max_points_slide_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of slide_max_pointsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function slide_max_pointsRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'slide_max_points'-------
    for (const thisComponent of slide_max_pointsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    max_points.setAutoDraw(false);
    
    psychoJS.experiment.addData('max_points_slide_key_resp.keys', max_points_slide_key_resp.keys);
    if (typeof max_points_slide_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('max_points_slide_key_resp.rt', max_points_slide_key_resp.rt);
        routineTimer.reset();
        }
    
    max_points_slide_key_resp.stop();
    // the Routine "slide_max_points" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _fractal_selection_quiz_key_resp_allKeys;
var fractal_selection_quizComponents;
function fractal_selection_quizRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'fractal_selection_quiz'-------
    t = 0;
    fractal_selection_quizClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    select_key_to_press_slide.setAutoDraw(true);
    
    fractal_selection_quiz_key_resp.keys = undefined;
    fractal_selection_quiz_key_resp.rt = undefined;
    _fractal_selection_quiz_key_resp_allKeys = [];
    // keep track of which components have finished
    fractal_selection_quizComponents = [];
    fractal_selection_quizComponents.push(fractal_selection_quiz_key_resp);
    
    for (const thisComponent of fractal_selection_quizComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function fractal_selection_quizRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'fractal_selection_quiz'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = fractal_selection_quizClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fractal_selection_quiz_key_resp* updates
    if (t >= 0.0 && fractal_selection_quiz_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fractal_selection_quiz_key_resp.tStart = t;  // (not accounting for frame time here)
      fractal_selection_quiz_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { fractal_selection_quiz_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { fractal_selection_quiz_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { fractal_selection_quiz_key_resp.clearEvents(); });
    }

    if (fractal_selection_quiz_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = fractal_selection_quiz_key_resp.getKeys({keyList: ['f', 'j'], waitRelease: false});
      _fractal_selection_quiz_key_resp_allKeys = _fractal_selection_quiz_key_resp_allKeys.concat(theseKeys);
      if (_fractal_selection_quiz_key_resp_allKeys.length > 0) {
        fractal_selection_quiz_key_resp.keys = _fractal_selection_quiz_key_resp_allKeys[_fractal_selection_quiz_key_resp_allKeys.length - 1].name;  // just the last key pressed
        fractal_selection_quiz_key_resp.rt = _fractal_selection_quiz_key_resp_allKeys[_fractal_selection_quiz_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of fractal_selection_quizComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var quiz_and_attention_check_fails;
function fractal_selection_quizRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'fractal_selection_quiz'-------
    for (const thisComponent of fractal_selection_quizComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    if (((fractal_selection_quiz_key_resp.keys === "f") && (select_key_to_press === 1))) {
        key_to_press_outcome = "correct";
        quiz_and_attention_check_fails = quiz_and_attention_check_fails;
    } else {
        if (((fractal_selection_quiz_key_resp.keys === "j") && (select_key_to_press === 1))) {
            key_to_press_outcome = "incorrect";
            quiz_and_attention_check_fails = (quiz_and_attention_check_fails + 1);
        } else {
            if (((fractal_selection_quiz_key_resp.keys === "f") && (select_key_to_press === 2))) {
                key_to_press_outcome = "incorrect";
                quiz_and_attention_check_fails = (quiz_and_attention_check_fails + 1);
            } else {
                if (((fractal_selection_quiz_key_resp.keys === "j") && (select_key_to_press === 2))) {
                    key_to_press_outcome = "correct";
                    quiz_and_attention_check_fails = quiz_and_attention_check_fails;
                }
            }
        }
    }
    select_key_to_press_slide.setAutoDraw(false);
    
    psychoJS.experiment.addData('fractal_selection_quiz_key_resp.keys', fractal_selection_quiz_key_resp.keys);
    if (typeof fractal_selection_quiz_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('fractal_selection_quiz_key_resp.rt', fractal_selection_quiz_key_resp.rt);
        routineTimer.reset();
        }
    
    fractal_selection_quiz_key_resp.stop();
    // the Routine "fractal_selection_quiz" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _fractal_reminder_show_key_resp_allKeys;
var fractal_reminder_showComponents;
function fractal_reminder_showRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'fractal_reminder_show'-------
    t = 0;
    fractal_reminder_showClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    if ((key_to_press_outcome === "correct")) {
        correct_fractal_reminder.setAutoDraw(true);
    } else {
        if ((key_to_press_outcome === "incorrect")) {
            incorrect_fractal_reminder.setAutoDraw(true);
        }
    }
    
    fractal_reminder_show_key_resp.keys = undefined;
    fractal_reminder_show_key_resp.rt = undefined;
    _fractal_reminder_show_key_resp_allKeys = [];
    // keep track of which components have finished
    fractal_reminder_showComponents = [];
    fractal_reminder_showComponents.push(fractal_reminder_show_key_resp);
    
    for (const thisComponent of fractal_reminder_showComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function fractal_reminder_showRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'fractal_reminder_show'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = fractal_reminder_showClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fractal_reminder_show_key_resp* updates
    if (t >= 0.0 && fractal_reminder_show_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fractal_reminder_show_key_resp.tStart = t;  // (not accounting for frame time here)
      fractal_reminder_show_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { fractal_reminder_show_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { fractal_reminder_show_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { fractal_reminder_show_key_resp.clearEvents(); });
    }

    if (fractal_reminder_show_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = fractal_reminder_show_key_resp.getKeys({keyList: [], waitRelease: false});
      _fractal_reminder_show_key_resp_allKeys = _fractal_reminder_show_key_resp_allKeys.concat(theseKeys);
      if (_fractal_reminder_show_key_resp_allKeys.length > 0) {
        fractal_reminder_show_key_resp.keys = _fractal_reminder_show_key_resp_allKeys[_fractal_reminder_show_key_resp_allKeys.length - 1].name;  // just the last key pressed
        fractal_reminder_show_key_resp.rt = _fractal_reminder_show_key_resp_allKeys[_fractal_reminder_show_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of fractal_reminder_showComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fractal_reminder_showRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'fractal_reminder_show'-------
    for (const thisComponent of fractal_reminder_showComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    if ((key_to_press_outcome === "correct")) {
        correct_fractal_reminder.setAutoDraw(false);
    } else {
        if ((key_to_press_outcome === "incorrect")) {
            incorrect_fractal_reminder.setAutoDraw(false);
        }
    }
    psychoJS.experiment.addData("key_to_press_outcome", key_to_press_outcome);
    
    psychoJS.experiment.addData('fractal_reminder_show_key_resp.keys', fractal_reminder_show_key_resp.keys);
    if (typeof fractal_reminder_show_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('fractal_reminder_show_key_resp.rt', fractal_reminder_show_key_resp.rt);
        routineTimer.reset();
        }
    
    fractal_reminder_show_key_resp.stop();
    // the Routine "fractal_reminder_show" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _slide_3_key_resp_allKeys;
var draw_slide_3Components;
function draw_slide_3RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'draw_slide_3'-------
    t = 0;
    draw_slide_3Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    instructions_slide_three.setAutoDraw(true);
    
    slide_3_key_resp.keys = undefined;
    slide_3_key_resp.rt = undefined;
    _slide_3_key_resp_allKeys = [];
    // keep track of which components have finished
    draw_slide_3Components = [];
    draw_slide_3Components.push(slide_3_key_resp);
    
    for (const thisComponent of draw_slide_3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function draw_slide_3RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'draw_slide_3'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = draw_slide_3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *slide_3_key_resp* updates
    if (t >= 0.0 && slide_3_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slide_3_key_resp.tStart = t;  // (not accounting for frame time here)
      slide_3_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { slide_3_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { slide_3_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { slide_3_key_resp.clearEvents(); });
    }

    if (slide_3_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = slide_3_key_resp.getKeys({keyList: [], waitRelease: false});
      _slide_3_key_resp_allKeys = _slide_3_key_resp_allKeys.concat(theseKeys);
      if (_slide_3_key_resp_allKeys.length > 0) {
        slide_3_key_resp.keys = _slide_3_key_resp_allKeys[_slide_3_key_resp_allKeys.length - 1].name;  // just the last key pressed
        slide_3_key_resp.rt = _slide_3_key_resp_allKeys[_slide_3_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of draw_slide_3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function draw_slide_3RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'draw_slide_3'-------
    for (const thisComponent of draw_slide_3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    instructions_slide_three.setAutoDraw(false);
    
    psychoJS.experiment.addData('slide_3_key_resp.keys', slide_3_key_resp.keys);
    if (typeof slide_3_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('slide_3_key_resp.rt', slide_3_key_resp.rt);
        routineTimer.reset();
        }
    
    slide_3_key_resp.stop();
    // the Routine "draw_slide_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _display_feedback_meanings_key_resp_allKeys;
var display_feedback_meaningsComponents;
function display_feedback_meaningsRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'display_feedback_meanings'-------
    t = 0;
    display_feedback_meaningsClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    if ((condition === 1)) {
        horizontal_feedback_stim.pos = [0, 0.12];
        vertical_feedback_stim.pos = [(- 0.17), 0.12];
        grey_no_feedback_stim.pos = [0.17, 0.12];
        horizontal_feedback_stim.size = [0.1, 0.12];
        vertical_feedback_stim.size = [0.1, 0.1];
        grey_no_feedback_stim.size = [0.1, 0.1];
        instructions_slide_four.setAutoDraw(true);
        horizontal_feedback_stim.setAutoDraw(true);
        vertical_feedback_stim.setAutoDraw(true);
        grey_no_feedback_stim.setAutoDraw(true);
    } else {
        if ((condition === 2)) {
            horizontal_feedback_stim.pos = [(- 0.17), 0.12];
            vertical_feedback_stim.pos = [0, 0.12];
            grey_no_feedback_stim.pos = [0.17, 0.12];
            horizontal_feedback_stim.size = [0.1, 0.1];
            vertical_feedback_stim.size = [0.1, 0.1];
            grey_no_feedback_stim.size = [0.1, 0.1];
            instructions_slide_four.setAutoDraw(true);
            horizontal_feedback_stim.setAutoDraw(true);
            vertical_feedback_stim.setAutoDraw(true);
            grey_no_feedback_stim.setAutoDraw(true);
        }
    }
    
    display_feedback_meanings_key_resp.keys = undefined;
    display_feedback_meanings_key_resp.rt = undefined;
    _display_feedback_meanings_key_resp_allKeys = [];
    // keep track of which components have finished
    display_feedback_meaningsComponents = [];
    display_feedback_meaningsComponents.push(display_feedback_meanings_key_resp);
    
    for (const thisComponent of display_feedback_meaningsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function display_feedback_meaningsRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'display_feedback_meanings'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = display_feedback_meaningsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *display_feedback_meanings_key_resp* updates
    if (t >= 0.0 && display_feedback_meanings_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      display_feedback_meanings_key_resp.tStart = t;  // (not accounting for frame time here)
      display_feedback_meanings_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { display_feedback_meanings_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { display_feedback_meanings_key_resp.start(); }); // start on screen flip
    }

    if (display_feedback_meanings_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = display_feedback_meanings_key_resp.getKeys({keyList: [], waitRelease: false});
      _display_feedback_meanings_key_resp_allKeys = _display_feedback_meanings_key_resp_allKeys.concat(theseKeys);
      if (_display_feedback_meanings_key_resp_allKeys.length > 0) {
        display_feedback_meanings_key_resp.keys = _display_feedback_meanings_key_resp_allKeys[_display_feedback_meanings_key_resp_allKeys.length - 1].name;  // just the last key pressed
        display_feedback_meanings_key_resp.rt = _display_feedback_meanings_key_resp_allKeys[_display_feedback_meanings_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of display_feedback_meaningsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function display_feedback_meaningsRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'display_feedback_meanings'-------
    for (const thisComponent of display_feedback_meaningsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    if ((condition === 1)) {
        horizontal_feedback_stim.pos = [0, 0.12];
        vertical_feedback_stim.pos = [(- 0.17), 0.12];
        grey_no_feedback_stim.pos = [0.17, 0.12];
        horizontal_feedback_stim.size = [0.1, 0.1];
        vertical_feedback_stim.size = [0.1, 0.1];
        grey_no_feedback_stim.size = [0.1, 0.1];
        instructions_slide_four.setAutoDraw(false);
        horizontal_feedback_stim.setAutoDraw(false);
        vertical_feedback_stim.setAutoDraw(false);
        grey_no_feedback_stim.setAutoDraw(false);
    } else {
        if ((condition === 2)) {
            horizontal_feedback_stim.pos = [(- 0.17), 0.12];
            vertical_feedback_stim.pos = [0, 0.12];
            grey_no_feedback_stim.pos = [0.17, 0.12];
            horizontal_feedback_stim.size = [0.1, 0.1];
            vertical_feedback_stim.size = [0.1, 0.1];
            grey_no_feedback_stim.size = [0.1, 0.1];
            instructions_slide_four.setAutoDraw(false);
            horizontal_feedback_stim.setAutoDraw(false);
            vertical_feedback_stim.setAutoDraw(false);
            grey_no_feedback_stim.setAutoDraw(false);
        }
    }
    
    psychoJS.experiment.addData('display_feedback_meanings_key_resp.keys', display_feedback_meanings_key_resp.keys);
    if (typeof display_feedback_meanings_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('display_feedback_meanings_key_resp.rt', display_feedback_meanings_key_resp.rt);
        routineTimer.reset();
        }
    
    display_feedback_meanings_key_resp.stop();
    // the Routine "display_feedback_meanings" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _first_quiz_first_question_key_resp_allKeys;
var first_quiz_first_questionComponents;
function first_quiz_first_questionRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'first_quiz_first_question'-------
    t = 0;
    first_quiz_first_questionClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    horizontal_feedback_stim.pos = [0, 0.12];
    horizontal_feedback_stim.size = [0.1, 0.1];
    instructions_slide_six.setAutoDraw(true);
    horizontal_feedback_stim.setAutoDraw(true);
    
    first_quiz_first_question_key_resp.keys = undefined;
    first_quiz_first_question_key_resp.rt = undefined;
    _first_quiz_first_question_key_resp_allKeys = [];
    // keep track of which components have finished
    first_quiz_first_questionComponents = [];
    first_quiz_first_questionComponents.push(first_quiz_first_question_key_resp);
    
    for (const thisComponent of first_quiz_first_questionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function first_quiz_first_questionRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'first_quiz_first_question'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = first_quiz_first_questionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *first_quiz_first_question_key_resp* updates
    if (t >= 0.0 && first_quiz_first_question_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      first_quiz_first_question_key_resp.tStart = t;  // (not accounting for frame time here)
      first_quiz_first_question_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { first_quiz_first_question_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { first_quiz_first_question_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { first_quiz_first_question_key_resp.clearEvents(); });
    }

    if (first_quiz_first_question_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = first_quiz_first_question_key_resp.getKeys({keyList: ['1', '2', '3'], waitRelease: false});
      _first_quiz_first_question_key_resp_allKeys = _first_quiz_first_question_key_resp_allKeys.concat(theseKeys);
      if (_first_quiz_first_question_key_resp_allKeys.length > 0) {
        first_quiz_first_question_key_resp.keys = _first_quiz_first_question_key_resp_allKeys[_first_quiz_first_question_key_resp_allKeys.length - 1].name;  // just the last key pressed
        first_quiz_first_question_key_resp.rt = _first_quiz_first_question_key_resp_allKeys[_first_quiz_first_question_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of first_quiz_first_questionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function first_quiz_first_questionRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'first_quiz_first_question'-------
    for (const thisComponent of first_quiz_first_questionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    if (((first_quiz_first_question_key_resp.keys === "1") && (condition === 1))) {
        quiz_and_attention_check_fails = (quiz_and_attention_check_fails + 1);
        first_stim_quiz_first_question_result = "incorrect";
    } else {
        if (((first_quiz_first_question_key_resp.keys === "2") && (condition === 1))) {
            quiz_and_attention_check_fails = quiz_and_attention_check_fails;
            first_stim_quiz_first_question_result = "correct";
        } else {
            if (((first_quiz_first_question_key_resp.keys === "3") && (condition === 1))) {
                quiz_and_attention_check_fails = (quiz_and_attention_check_fails + 1);
                first_stim_quiz_first_question_result = "incorrect";
            } else {
                if (((first_quiz_first_question_key_resp.keys === "1") && (condition === 2))) {
                    quiz_and_attention_check_fails = quiz_and_attention_check_fails;
                    first_stim_quiz_first_question_result = "correct";
                } else {
                    if (((first_quiz_first_question_key_resp.keys === "2") && (condition === 2))) {
                        quiz_and_attention_check_fails = (quiz_and_attention_check_fails + 1);
                        first_stim_quiz_first_question_result = "incorrect";
                    } else {
                        if (((first_quiz_first_question_key_resp.keys === "3") && (condition === 2))) {
                            quiz_and_attention_check_fails = (quiz_and_attention_check_fails + 1);
                            first_stim_quiz_first_question_result = "incorrect";
                        }
                    }
                }
            }
        }
    }
    horizontal_feedback_stim.pos = [0, 0.12];
    horizontal_feedback_stim.size = [0.1, 0.1];
    instructions_slide_six.setAutoDraw(false);
    horizontal_feedback_stim.setAutoDraw(false);
    
    psychoJS.experiment.addData('first_quiz_first_question_key_resp.keys', first_quiz_first_question_key_resp.keys);
    if (typeof first_quiz_first_question_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('first_quiz_first_question_key_resp.rt', first_quiz_first_question_key_resp.rt);
        routineTimer.reset();
        }
    
    first_quiz_first_question_key_resp.stop();
    // the Routine "first_quiz_first_question" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _first_quiz_first_q_reminder_key_resp_allKeys;
var first_quiz_first_question_reminderComponents;
function first_quiz_first_question_reminderRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'first_quiz_first_question_reminder'-------
    t = 0;
    first_quiz_first_question_reminderClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    if (((first_stim_quiz_first_question_result === "correct") && (condition === 1))) {
        horizontal_feedback_stim.pos = [0, 0.12];
        horizontal_feedback_stim.size = [0.1, 0.1];
        correct_result_plus_zero.setAutoDraw(true);
        horizontal_feedback_stim.setAutoDraw(true);
    } else {
        if (((first_stim_quiz_first_question_result === "incorrect") && (condition === 1))) {
            horizontal_feedback_stim.pos = [0, 0.12];
            horizontal_feedback_stim.size = [0.1, 0.1];
            incorrect_result_plus_zero.setAutoDraw(true);
            horizontal_feedback_stim.setAutoDraw(true);
        } else {
            if (((first_stim_quiz_first_question_result === "correct") && (condition === 2))) {
                horizontal_feedback_stim.pos = [0, 0.12];
                horizontal_feedback_stim.size = [0.1, 0.1];
                correct_result_plus_one.setAutoDraw(true);
                horizontal_feedback_stim.setAutoDraw(true);
            } else {
                if (((first_stim_quiz_first_question_result === "incorrect") && (condition === 2))) {
                    horizontal_feedback_stim.pos = [0, 0.12];
                    horizontal_feedback_stim.size = [0.1, 0.1];
                    incorrect_result_plus_one.setAutoDraw(true);
                    horizontal_feedback_stim.setAutoDraw(true);
                }
            }
        }
    }
    
    first_quiz_first_q_reminder_key_resp.keys = undefined;
    first_quiz_first_q_reminder_key_resp.rt = undefined;
    _first_quiz_first_q_reminder_key_resp_allKeys = [];
    // keep track of which components have finished
    first_quiz_first_question_reminderComponents = [];
    first_quiz_first_question_reminderComponents.push(first_quiz_first_q_reminder_key_resp);
    
    for (const thisComponent of first_quiz_first_question_reminderComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function first_quiz_first_question_reminderRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'first_quiz_first_question_reminder'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = first_quiz_first_question_reminderClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *first_quiz_first_q_reminder_key_resp* updates
    if (t >= 0.0 && first_quiz_first_q_reminder_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      first_quiz_first_q_reminder_key_resp.tStart = t;  // (not accounting for frame time here)
      first_quiz_first_q_reminder_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { first_quiz_first_q_reminder_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { first_quiz_first_q_reminder_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { first_quiz_first_q_reminder_key_resp.clearEvents(); });
    }

    if (first_quiz_first_q_reminder_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = first_quiz_first_q_reminder_key_resp.getKeys({keyList: [], waitRelease: false});
      _first_quiz_first_q_reminder_key_resp_allKeys = _first_quiz_first_q_reminder_key_resp_allKeys.concat(theseKeys);
      if (_first_quiz_first_q_reminder_key_resp_allKeys.length > 0) {
        first_quiz_first_q_reminder_key_resp.keys = _first_quiz_first_q_reminder_key_resp_allKeys[_first_quiz_first_q_reminder_key_resp_allKeys.length - 1].name;  // just the last key pressed
        first_quiz_first_q_reminder_key_resp.rt = _first_quiz_first_q_reminder_key_resp_allKeys[_first_quiz_first_q_reminder_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of first_quiz_first_question_reminderComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function first_quiz_first_question_reminderRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'first_quiz_first_question_reminder'-------
    for (const thisComponent of first_quiz_first_question_reminderComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    if (((first_stim_quiz_first_question_result === "correct") && (condition === 1))) {
        horizontal_feedback_stim.pos = [0, 0.12];
        horizontal_feedback_stim.size = [0.1, 0.1];
        correct_result_plus_zero.setAutoDraw(false);
        horizontal_feedback_stim.setAutoDraw(false);
    } else {
        if (((first_stim_quiz_first_question_result === "incorrect") && (condition === 1))) {
            horizontal_feedback_stim.pos = [0, 0.12];
            horizontal_feedback_stim.size = [0.1, 0.1];
            incorrect_result_plus_zero.setAutoDraw(false);
            horizontal_feedback_stim.setAutoDraw(false);
        } else {
            if (((first_stim_quiz_first_question_result === "correct") && (condition === 2))) {
                horizontal_feedback_stim.pos = [0, 0.12];
                horizontal_feedback_stim.size = [0.1, 0.1];
                correct_result_plus_one.setAutoDraw(false);
                horizontal_feedback_stim.setAutoDraw(false);
            } else {
                if (((first_stim_quiz_first_question_result === "incorrect") && (condition === 2))) {
                    horizontal_feedback_stim.pos = [0, 0.12];
                    horizontal_feedback_stim.size = [0.1, 0.1];
                    incorrect_result_plus_one.setAutoDraw(false);
                    horizontal_feedback_stim.setAutoDraw(false);
                }
            }
        }
    }
    
    psychoJS.experiment.addData('first_quiz_first_q_reminder_key_resp.keys', first_quiz_first_q_reminder_key_resp.keys);
    if (typeof first_quiz_first_q_reminder_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('first_quiz_first_q_reminder_key_resp.rt', first_quiz_first_q_reminder_key_resp.rt);
        routineTimer.reset();
        }
    
    first_quiz_first_q_reminder_key_resp.stop();
    // the Routine "first_quiz_first_question_reminder" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _first_quiz_second_question_key_resp_allKeys;
var first_quiz_second_questionComponents;
function first_quiz_second_questionRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'first_quiz_second_question'-------
    t = 0;
    first_quiz_second_questionClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    grey_no_feedback_stim.pos = [0, 0.12];
    grey_no_feedback_stim.size = [0.1, 0.1];
    instructions_slide_six.setAutoDraw(true);
    grey_no_feedback_stim.setAutoDraw(true);
    
    first_quiz_second_question_key_resp.keys = undefined;
    first_quiz_second_question_key_resp.rt = undefined;
    _first_quiz_second_question_key_resp_allKeys = [];
    // keep track of which components have finished
    first_quiz_second_questionComponents = [];
    first_quiz_second_questionComponents.push(first_quiz_second_question_key_resp);
    
    for (const thisComponent of first_quiz_second_questionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function first_quiz_second_questionRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'first_quiz_second_question'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = first_quiz_second_questionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *first_quiz_second_question_key_resp* updates
    if (t >= 0.0 && first_quiz_second_question_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      first_quiz_second_question_key_resp.tStart = t;  // (not accounting for frame time here)
      first_quiz_second_question_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { first_quiz_second_question_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { first_quiz_second_question_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { first_quiz_second_question_key_resp.clearEvents(); });
    }

    if (first_quiz_second_question_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = first_quiz_second_question_key_resp.getKeys({keyList: ['1', '2', '3'], waitRelease: false});
      _first_quiz_second_question_key_resp_allKeys = _first_quiz_second_question_key_resp_allKeys.concat(theseKeys);
      if (_first_quiz_second_question_key_resp_allKeys.length > 0) {
        first_quiz_second_question_key_resp.keys = _first_quiz_second_question_key_resp_allKeys[_first_quiz_second_question_key_resp_allKeys.length - 1].name;  // just the last key pressed
        first_quiz_second_question_key_resp.rt = _first_quiz_second_question_key_resp_allKeys[_first_quiz_second_question_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of first_quiz_second_questionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function first_quiz_second_questionRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'first_quiz_second_question'-------
    for (const thisComponent of first_quiz_second_questionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    if ((first_quiz_second_question_key_resp.keys === "1")) {
        quiz_and_attention_check_fails = (quiz_and_attention_check_fails + 1);
        first_stim_quiz_second_question_result = "incorrect";
    } else {
        if ((first_quiz_second_question_key_resp.keys === "2")) {
            quiz_and_attention_check_fails = (quiz_and_attention_check_fails + 1);
            first_stim_quiz_second_question_result = "incorrect";
        } else {
            if ((first_quiz_second_question_key_resp.keys === "3")) {
                quiz_and_attention_check_fails = quiz_and_attention_check_fails;
                first_stim_quiz_second_question_result = "correct";
            }
        }
    }
    grey_no_feedback_stim.pos = [0, 0.12];
    grey_no_feedback_stim.size = [0.1, 0.1];
    instructions_slide_six.setAutoDraw(false);
    grey_no_feedback_stim.setAutoDraw(false);
    
    psychoJS.experiment.addData('first_quiz_second_question_key_resp.keys', first_quiz_second_question_key_resp.keys);
    if (typeof first_quiz_second_question_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('first_quiz_second_question_key_resp.rt', first_quiz_second_question_key_resp.rt);
        routineTimer.reset();
        }
    
    first_quiz_second_question_key_resp.stop();
    // the Routine "first_quiz_second_question" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _first_quiz_second_question_reminder_key_resp_allKeys;
var first_quiz_second_question_reminderComponents;
function first_quiz_second_question_reminderRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'first_quiz_second_question_reminder'-------
    t = 0;
    first_quiz_second_question_reminderClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    if ((first_stim_quiz_second_question_result === "correct")) {
        grey_no_feedback_stim.pos = [0, 0.12];
        grey_no_feedback_stim.size = [0.1, 0.1];
        correct_result_no_feedback.setAutoDraw(true);
        grey_no_feedback_stim.setAutoDraw(true);
    } else {
        if ((first_stim_quiz_second_question_result === "incorrect")) {
            grey_no_feedback_stim.pos = [0, 0.12];
            grey_no_feedback_stim.size = [0.1, 0.1];
            incorrect_result_no_feedback.setAutoDraw(true);
            grey_no_feedback_stim.setAutoDraw(true);
        }
    }
    
    first_quiz_second_question_reminder_key_resp.keys = undefined;
    first_quiz_second_question_reminder_key_resp.rt = undefined;
    _first_quiz_second_question_reminder_key_resp_allKeys = [];
    // keep track of which components have finished
    first_quiz_second_question_reminderComponents = [];
    first_quiz_second_question_reminderComponents.push(first_quiz_second_question_reminder_key_resp);
    
    for (const thisComponent of first_quiz_second_question_reminderComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function first_quiz_second_question_reminderRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'first_quiz_second_question_reminder'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = first_quiz_second_question_reminderClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *first_quiz_second_question_reminder_key_resp* updates
    if (t >= 0.0 && first_quiz_second_question_reminder_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      first_quiz_second_question_reminder_key_resp.tStart = t;  // (not accounting for frame time here)
      first_quiz_second_question_reminder_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { first_quiz_second_question_reminder_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { first_quiz_second_question_reminder_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { first_quiz_second_question_reminder_key_resp.clearEvents(); });
    }

    if (first_quiz_second_question_reminder_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = first_quiz_second_question_reminder_key_resp.getKeys({keyList: [], waitRelease: false});
      _first_quiz_second_question_reminder_key_resp_allKeys = _first_quiz_second_question_reminder_key_resp_allKeys.concat(theseKeys);
      if (_first_quiz_second_question_reminder_key_resp_allKeys.length > 0) {
        first_quiz_second_question_reminder_key_resp.keys = _first_quiz_second_question_reminder_key_resp_allKeys[_first_quiz_second_question_reminder_key_resp_allKeys.length - 1].name;  // just the last key pressed
        first_quiz_second_question_reminder_key_resp.rt = _first_quiz_second_question_reminder_key_resp_allKeys[_first_quiz_second_question_reminder_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of first_quiz_second_question_reminderComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function first_quiz_second_question_reminderRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'first_quiz_second_question_reminder'-------
    for (const thisComponent of first_quiz_second_question_reminderComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    if ((first_stim_quiz_second_question_result === "correct")) {
        grey_no_feedback_stim.pos = [0, 0.12];
        grey_no_feedback_stim.size = [0.1, 0.1];
        correct_result_no_feedback.setAutoDraw(false);
        grey_no_feedback_stim.setAutoDraw(false);
    } else {
        if ((first_stim_quiz_second_question_result === "incorrect")) {
            grey_no_feedback_stim.pos = [0, 0.12];
            grey_no_feedback_stim.size = [0.1, 0.1];
            incorrect_result_no_feedback.setAutoDraw(false);
            grey_no_feedback_stim.setAutoDraw(false);
        }
    }
    
    psychoJS.experiment.addData('first_quiz_second_question_reminder_key_resp.keys', first_quiz_second_question_reminder_key_resp.keys);
    if (typeof first_quiz_second_question_reminder_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('first_quiz_second_question_reminder_key_resp.rt', first_quiz_second_question_reminder_key_resp.rt);
        routineTimer.reset();
        }
    
    first_quiz_second_question_reminder_key_resp.stop();
    // the Routine "first_quiz_second_question_reminder" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _last_q_first_quiz_key_resp_allKeys;
var first_quiz_third_questionComponents;
function first_quiz_third_questionRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'first_quiz_third_question'-------
    t = 0;
    first_quiz_third_questionClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    last_q_first_quiz_key_resp.keys = undefined;
    last_q_first_quiz_key_resp.rt = undefined;
    _last_q_first_quiz_key_resp_allKeys = [];
    vertical_feedback_stim.pos = [0, 0.12];
    vertical_feedback_stim.size = [0.1, 0.1];
    instructions_slide_six.setAutoDraw(true);
    vertical_feedback_stim.setAutoDraw(true);
    
    // keep track of which components have finished
    first_quiz_third_questionComponents = [];
    first_quiz_third_questionComponents.push(last_q_first_quiz_key_resp);
    
    for (const thisComponent of first_quiz_third_questionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function first_quiz_third_questionRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'first_quiz_third_question'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = first_quiz_third_questionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *last_q_first_quiz_key_resp* updates
    if (t >= 0.0 && last_q_first_quiz_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      last_q_first_quiz_key_resp.tStart = t;  // (not accounting for frame time here)
      last_q_first_quiz_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { last_q_first_quiz_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { last_q_first_quiz_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { last_q_first_quiz_key_resp.clearEvents(); });
    }

    if (last_q_first_quiz_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = last_q_first_quiz_key_resp.getKeys({keyList: ['1', '2', '3'], waitRelease: false});
      _last_q_first_quiz_key_resp_allKeys = _last_q_first_quiz_key_resp_allKeys.concat(theseKeys);
      if (_last_q_first_quiz_key_resp_allKeys.length > 0) {
        last_q_first_quiz_key_resp.keys = _last_q_first_quiz_key_resp_allKeys[_last_q_first_quiz_key_resp_allKeys.length - 1].name;  // just the last key pressed
        last_q_first_quiz_key_resp.rt = _last_q_first_quiz_key_resp_allKeys[_last_q_first_quiz_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of first_quiz_third_questionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function first_quiz_third_questionRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'first_quiz_third_question'-------
    for (const thisComponent of first_quiz_third_questionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('last_q_first_quiz_key_resp.keys', last_q_first_quiz_key_resp.keys);
    if (typeof last_q_first_quiz_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('last_q_first_quiz_key_resp.rt', last_q_first_quiz_key_resp.rt);
        routineTimer.reset();
        }
    
    last_q_first_quiz_key_resp.stop();
    if (((last_q_first_quiz_key_resp.keys === "1") && (condition === 1))) {
        quiz_and_attention_check_fails = quiz_and_attention_check_fails;
        first_stim_quiz_third_question_result = "correct";
    } else {
        if (((last_q_first_quiz_key_resp.keys === "2") && (condition === 1))) {
            quiz_and_attention_check_fails = (quiz_and_attention_check_fails + 1);
            first_stim_quiz_third_question_result = "incorrect";
        } else {
            if (((last_q_first_quiz_key_resp.keys === "3") && (condition === 1))) {
                quiz_and_attention_check_fails = (quiz_and_attention_check_fails + 1);
                first_stim_quiz_third_question_result = "incorrect";
            } else {
                if (((last_q_first_quiz_key_resp.keys === "1") && (condition === 2))) {
                    quiz_and_attention_check_fails = (quiz_and_attention_check_fails + 1);
                    first_stim_quiz_third_question_result = "incorrect";
                } else {
                    if (((last_q_first_quiz_key_resp.keys === "2") && (condition === 2))) {
                        quiz_and_attention_check_fails = quiz_and_attention_check_fails;
                        first_stim_quiz_third_question_result = "correct";
                    } else {
                        if (((last_q_first_quiz_key_resp.keys === "3") && (condition === 2))) {
                            quiz_and_attention_check_fails = (quiz_and_attention_check_fails + 1);
                            first_stim_quiz_third_question_result = "incorrect";
                        }
                    }
                }
            }
        }
    }
    vertical_feedback_stim.pos = [0, 0.12];
    vertical_feedback_stim.size = [0.1, 0.1];
    instructions_slide_six.setAutoDraw(false);
    vertical_feedback_stim.setAutoDraw(false);
    
    // the Routine "first_quiz_third_question" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _first_quiz_third_question_reminder_key_resp_allKeys;
var first_quiz_third_question_reminderComponents;
function first_quiz_third_question_reminderRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'first_quiz_third_question_reminder'-------
    t = 0;
    first_quiz_third_question_reminderClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    first_quiz_third_question_reminder_key_resp.keys = undefined;
    first_quiz_third_question_reminder_key_resp.rt = undefined;
    _first_quiz_third_question_reminder_key_resp_allKeys = [];
    if (((first_stim_quiz_third_question_result === "correct") && (condition === 1))) {
        vertical_feedback_stim.pos = [0, 0.12];
        vertical_feedback_stim.size = [0.1, 0.1];
        correct_result_plus_one.setAutoDraw(true);
        vertical_feedback_stim.setAutoDraw(true);
    } else {
        if (((first_stim_quiz_third_question_result === "incorrect") && (condition === 1))) {
            vertical_feedback_stim.pos = [0, 0.12];
            vertical_feedback_stim.size = [0.1, 0.1];
            incorrect_result_plus_one.setAutoDraw(true);
            vertical_feedback_stim.setAutoDraw(true);
        } else {
            if (((first_stim_quiz_third_question_result === "correct") && (condition === 2))) {
                vertical_feedback_stim.pos = [0, 0.12];
                vertical_feedback_stim.size = [0.1, 0.1];
                correct_result_plus_zero.setAutoDraw(true);
                vertical_feedback_stim.setAutoDraw(true);
            } else {
                if (((first_stim_quiz_third_question_result === "incorrect") && (condition === 2))) {
                    vertical_feedback_stim.pos = [0, 0.12];
                    vertical_feedback_stim.size = [0.1, 0.1];
                    incorrect_result_plus_zero.setAutoDraw(true);
                    vertical_feedback_stim.setAutoDraw(true);
                }
            }
        }
    }
    
    // keep track of which components have finished
    first_quiz_third_question_reminderComponents = [];
    first_quiz_third_question_reminderComponents.push(first_quiz_third_question_reminder_key_resp);
    
    for (const thisComponent of first_quiz_third_question_reminderComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function first_quiz_third_question_reminderRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'first_quiz_third_question_reminder'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = first_quiz_third_question_reminderClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *first_quiz_third_question_reminder_key_resp* updates
    if (t >= 0.0 && first_quiz_third_question_reminder_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      first_quiz_third_question_reminder_key_resp.tStart = t;  // (not accounting for frame time here)
      first_quiz_third_question_reminder_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { first_quiz_third_question_reminder_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { first_quiz_third_question_reminder_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { first_quiz_third_question_reminder_key_resp.clearEvents(); });
    }

    if (first_quiz_third_question_reminder_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = first_quiz_third_question_reminder_key_resp.getKeys({keyList: [], waitRelease: false});
      _first_quiz_third_question_reminder_key_resp_allKeys = _first_quiz_third_question_reminder_key_resp_allKeys.concat(theseKeys);
      if (_first_quiz_third_question_reminder_key_resp_allKeys.length > 0) {
        first_quiz_third_question_reminder_key_resp.keys = _first_quiz_third_question_reminder_key_resp_allKeys[_first_quiz_third_question_reminder_key_resp_allKeys.length - 1].name;  // just the last key pressed
        first_quiz_third_question_reminder_key_resp.rt = _first_quiz_third_question_reminder_key_resp_allKeys[_first_quiz_third_question_reminder_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of first_quiz_third_question_reminderComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function first_quiz_third_question_reminderRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'first_quiz_third_question_reminder'-------
    for (const thisComponent of first_quiz_third_question_reminderComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('first_quiz_third_question_reminder_key_resp.keys', first_quiz_third_question_reminder_key_resp.keys);
    if (typeof first_quiz_third_question_reminder_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('first_quiz_third_question_reminder_key_resp.rt', first_quiz_third_question_reminder_key_resp.rt);
        routineTimer.reset();
        }
    
    first_quiz_third_question_reminder_key_resp.stop();
    if (((first_stim_quiz_third_question_result === "correct") && (condition === 1))) {
        vertical_feedback_stim.pos = [0, 0.12];
        vertical_feedback_stim.size = [0.1, 0.1];
        correct_result_plus_one.setAutoDraw(false);
        vertical_feedback_stim.setAutoDraw(false);
    } else {
        if (((first_stim_quiz_third_question_result === "incorrect") && (condition === 1))) {
            vertical_feedback_stim.pos = [0, 0.12];
            vertical_feedback_stim.size = [0.1, 0.1];
            incorrect_result_plus_one.setAutoDraw(false);
            vertical_feedback_stim.setAutoDraw(false);
        } else {
            if (((first_stim_quiz_third_question_result === "correct") && (condition === 2))) {
                vertical_feedback_stim.pos = [0, 0.12];
                vertical_feedback_stim.size = [0.1, 0.1];
                correct_result_plus_zero.setAutoDraw(false);
                vertical_feedback_stim.setAutoDraw(false);
            } else {
                if (((first_stim_quiz_third_question_result === "incorrect") && (condition === 2))) {
                    vertical_feedback_stim.pos = [0, 0.12];
                    vertical_feedback_stim.size = [0.1, 0.1];
                    incorrect_result_plus_zero.setAutoDraw(false);
                    vertical_feedback_stim.setAutoDraw(false);
                }
            }
        }
    }
    
    // the Routine "first_quiz_third_question_reminder" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _first_reminder_key_resp_allKeys;
var total_reminder_oneComponents;
function total_reminder_oneRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'total_reminder_one'-------
    t = 0;
    total_reminder_oneClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    first_reminder_key_resp.keys = undefined;
    first_reminder_key_resp.rt = undefined;
    _first_reminder_key_resp_allKeys = [];
    if ((condition === 1)) {
        horizontal_feedback_stim.pos = [0, 0.17];
        vertical_feedback_stim.pos = [(- 0.17), 0.17];
        grey_no_feedback_stim.pos = [0.17, 0.17];
        horizontal_feedback_stim.size = [0.1, 0.1];
        vertical_feedback_stim.size = [0.1, 0.1];
        grey_no_feedback_stim.size = [0.1, 0.1];
        result_final_reminder.setAutoDraw(true);
        horizontal_feedback_stim.setAutoDraw(true);
        vertical_feedback_stim.setAutoDraw(true);
        grey_no_feedback_stim.setAutoDraw(true);
    } else {
        if ((condition === 2)) {
            horizontal_feedback_stim.pos = [(- 0.17), 0.17];
            vertical_feedback_stim.pos = [0, 0.17];
            grey_no_feedback_stim.pos = [0.17, 0.17];
            horizontal_feedback_stim.size = [0.1, 0.1];
            vertical_feedback_stim.size = [0.1, 0.1];
            grey_no_feedback_stim.size = [0.1, 0.1];
            result_final_reminder.setAutoDraw(true);
            horizontal_feedback_stim.setAutoDraw(true);
            vertical_feedback_stim.setAutoDraw(true);
            grey_no_feedback_stim.setAutoDraw(true);
        }
    }
    
    // keep track of which components have finished
    total_reminder_oneComponents = [];
    total_reminder_oneComponents.push(first_reminder_key_resp);
    
    for (const thisComponent of total_reminder_oneComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function total_reminder_oneRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'total_reminder_one'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = total_reminder_oneClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *first_reminder_key_resp* updates
    if (t >= 0.0 && first_reminder_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      first_reminder_key_resp.tStart = t;  // (not accounting for frame time here)
      first_reminder_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { first_reminder_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { first_reminder_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { first_reminder_key_resp.clearEvents(); });
    }

    if (first_reminder_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = first_reminder_key_resp.getKeys({keyList: [], waitRelease: false});
      _first_reminder_key_resp_allKeys = _first_reminder_key_resp_allKeys.concat(theseKeys);
      if (_first_reminder_key_resp_allKeys.length > 0) {
        first_reminder_key_resp.keys = _first_reminder_key_resp_allKeys[_first_reminder_key_resp_allKeys.length - 1].name;  // just the last key pressed
        first_reminder_key_resp.rt = _first_reminder_key_resp_allKeys[_first_reminder_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of total_reminder_oneComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function total_reminder_oneRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'total_reminder_one'-------
    for (const thisComponent of total_reminder_oneComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('first_reminder_key_resp.keys', first_reminder_key_resp.keys);
    if (typeof first_reminder_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('first_reminder_key_resp.rt', first_reminder_key_resp.rt);
        routineTimer.reset();
        }
    
    first_reminder_key_resp.stop();
    if ((condition === 1)) {
        horizontal_feedback_stim.pos = [0, 0.17];
        vertical_feedback_stim.pos = [(- 0.17), 0.17];
        grey_no_feedback_stim.pos = [0.17, 0.17];
        horizontal_feedback_stim.size = [0.1, 0.1];
        vertical_feedback_stim.size = [0.1, 0.1];
        grey_no_feedback_stim.size = [0.1, 0.1];
        result_final_reminder.setAutoDraw(false);
        horizontal_feedback_stim.setAutoDraw(false);
        vertical_feedback_stim.setAutoDraw(false);
        grey_no_feedback_stim.setAutoDraw(false);
    } else {
        if ((condition === 2)) {
            horizontal_feedback_stim.pos = [(- 0.17), 0.17];
            vertical_feedback_stim.pos = [0, 0.17];
            grey_no_feedback_stim.pos = [0.17, 0.17];
            horizontal_feedback_stim.size = [0.1, 0.1];
            vertical_feedback_stim.size = [0.1, 0.1];
            grey_no_feedback_stim.size = [0.1, 0.1];
            result_final_reminder.setAutoDraw(false);
            horizontal_feedback_stim.setAutoDraw(false);
            vertical_feedback_stim.setAutoDraw(false);
            grey_no_feedback_stim.setAutoDraw(false);
        }
    }
    psychoJS.experiment.addData("first_stim_quiz_first_question_result", first_stim_quiz_first_question_result);
    psychoJS.experiment.addData("first_stim_quiz_second_question_result", first_stim_quiz_second_question_result);
    psychoJS.experiment.addData("first_stim_quiz_third_question_result", first_stim_quiz_third_question_result);
    
    // the Routine "total_reminder_one" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _slide_8_01_key_resp_allKeys;
var continue_instructions_8_01Components;
function continue_instructions_8_01RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'continue_instructions_8_01'-------
    t = 0;
    continue_instructions_8_01Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    instructions_slide_8_01.setAutoDraw(true);
    
    slide_8_01_key_resp.keys = undefined;
    slide_8_01_key_resp.rt = undefined;
    _slide_8_01_key_resp_allKeys = [];
    // keep track of which components have finished
    continue_instructions_8_01Components = [];
    continue_instructions_8_01Components.push(slide_8_01_key_resp);
    
    for (const thisComponent of continue_instructions_8_01Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function continue_instructions_8_01RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'continue_instructions_8_01'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = continue_instructions_8_01Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *slide_8_01_key_resp* updates
    if (t >= 0.0 && slide_8_01_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slide_8_01_key_resp.tStart = t;  // (not accounting for frame time here)
      slide_8_01_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { slide_8_01_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { slide_8_01_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { slide_8_01_key_resp.clearEvents(); });
    }

    if (slide_8_01_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = slide_8_01_key_resp.getKeys({keyList: [], waitRelease: false});
      _slide_8_01_key_resp_allKeys = _slide_8_01_key_resp_allKeys.concat(theseKeys);
      if (_slide_8_01_key_resp_allKeys.length > 0) {
        slide_8_01_key_resp.keys = _slide_8_01_key_resp_allKeys[_slide_8_01_key_resp_allKeys.length - 1].name;  // just the last key pressed
        slide_8_01_key_resp.rt = _slide_8_01_key_resp_allKeys[_slide_8_01_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of continue_instructions_8_01Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function continue_instructions_8_01RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'continue_instructions_8_01'-------
    for (const thisComponent of continue_instructions_8_01Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    instructions_slide_8_01.setAutoDraw(false);
    
    psychoJS.experiment.addData('slide_8_01_key_resp.keys', slide_8_01_key_resp.keys);
    if (typeof slide_8_01_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('slide_8_01_key_resp.rt', slide_8_01_key_resp.rt);
        routineTimer.reset();
        }
    
    slide_8_01_key_resp.stop();
    // the Routine "continue_instructions_8_01" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _slide_8_02_key_resp_allKeys;
var continue_instructions_8_02Components;
function continue_instructions_8_02RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'continue_instructions_8_02'-------
    t = 0;
    continue_instructions_8_02Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    instructions_slide_8_02.setAutoDraw(true);
    
    slide_8_02_key_resp.keys = undefined;
    slide_8_02_key_resp.rt = undefined;
    _slide_8_02_key_resp_allKeys = [];
    // keep track of which components have finished
    continue_instructions_8_02Components = [];
    continue_instructions_8_02Components.push(slide_8_02_key_resp);
    
    for (const thisComponent of continue_instructions_8_02Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function continue_instructions_8_02RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'continue_instructions_8_02'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = continue_instructions_8_02Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *slide_8_02_key_resp* updates
    if (t >= 0.0 && slide_8_02_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slide_8_02_key_resp.tStart = t;  // (not accounting for frame time here)
      slide_8_02_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { slide_8_02_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { slide_8_02_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { slide_8_02_key_resp.clearEvents(); });
    }

    if (slide_8_02_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = slide_8_02_key_resp.getKeys({keyList: [], waitRelease: false});
      _slide_8_02_key_resp_allKeys = _slide_8_02_key_resp_allKeys.concat(theseKeys);
      if (_slide_8_02_key_resp_allKeys.length > 0) {
        slide_8_02_key_resp.keys = _slide_8_02_key_resp_allKeys[_slide_8_02_key_resp_allKeys.length - 1].name;  // just the last key pressed
        slide_8_02_key_resp.rt = _slide_8_02_key_resp_allKeys[_slide_8_02_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of continue_instructions_8_02Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function continue_instructions_8_02RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'continue_instructions_8_02'-------
    for (const thisComponent of continue_instructions_8_02Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    instructions_slide_8_02.setAutoDraw(false);
    
    psychoJS.experiment.addData('slide_8_02_key_resp.keys', slide_8_02_key_resp.keys);
    if (typeof slide_8_02_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('slide_8_02_key_resp.rt', slide_8_02_key_resp.rt);
        routineTimer.reset();
        }
    
    slide_8_02_key_resp.stop();
    // the Routine "continue_instructions_8_02" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _slide_8_03_key_resp_allKeys;
var continue_instructions_8_03Components;
function continue_instructions_8_03RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'continue_instructions_8_03'-------
    t = 0;
    continue_instructions_8_03Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    instructions_slide_8_03.setAutoDraw(true);
    
    slide_8_03_key_resp.keys = undefined;
    slide_8_03_key_resp.rt = undefined;
    _slide_8_03_key_resp_allKeys = [];
    // keep track of which components have finished
    continue_instructions_8_03Components = [];
    continue_instructions_8_03Components.push(slide_8_03_key_resp);
    
    for (const thisComponent of continue_instructions_8_03Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function continue_instructions_8_03RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'continue_instructions_8_03'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = continue_instructions_8_03Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *slide_8_03_key_resp* updates
    if (t >= 0.0 && slide_8_03_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slide_8_03_key_resp.tStart = t;  // (not accounting for frame time here)
      slide_8_03_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { slide_8_03_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { slide_8_03_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { slide_8_03_key_resp.clearEvents(); });
    }

    if (slide_8_03_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = slide_8_03_key_resp.getKeys({keyList: [], waitRelease: false});
      _slide_8_03_key_resp_allKeys = _slide_8_03_key_resp_allKeys.concat(theseKeys);
      if (_slide_8_03_key_resp_allKeys.length > 0) {
        slide_8_03_key_resp.keys = _slide_8_03_key_resp_allKeys[_slide_8_03_key_resp_allKeys.length - 1].name;  // just the last key pressed
        slide_8_03_key_resp.rt = _slide_8_03_key_resp_allKeys[_slide_8_03_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of continue_instructions_8_03Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function continue_instructions_8_03RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'continue_instructions_8_03'-------
    for (const thisComponent of continue_instructions_8_03Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    instructions_slide_8_03.setAutoDraw(false);
    
    psychoJS.experiment.addData('slide_8_03_key_resp.keys', slide_8_03_key_resp.keys);
    if (typeof slide_8_03_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('slide_8_03_key_resp.rt', slide_8_03_key_resp.rt);
        routineTimer.reset();
        }
    
    slide_8_03_key_resp.stop();
    // the Routine "continue_instructions_8_03" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _feedback_selection_quiz_key_resp_allKeys;
var feedback_selection_quizComponents;
function feedback_selection_quizRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'feedback_selection_quiz'-------
    t = 0;
    feedback_selection_quizClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    select_feedback_to_press_slide.setAutoDraw(true);
    
    feedback_selection_quiz_key_resp.keys = undefined;
    feedback_selection_quiz_key_resp.rt = undefined;
    _feedback_selection_quiz_key_resp_allKeys = [];
    // keep track of which components have finished
    feedback_selection_quizComponents = [];
    feedback_selection_quizComponents.push(feedback_selection_quiz_key_resp);
    
    for (const thisComponent of feedback_selection_quizComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function feedback_selection_quizRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'feedback_selection_quiz'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = feedback_selection_quizClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_selection_quiz_key_resp* updates
    if (t >= 0.0 && feedback_selection_quiz_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_selection_quiz_key_resp.tStart = t;  // (not accounting for frame time here)
      feedback_selection_quiz_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      feedback_selection_quiz_key_resp.clock.reset();
      feedback_selection_quiz_key_resp.start();
      feedback_selection_quiz_key_resp.clearEvents();
    }

    if (feedback_selection_quiz_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = feedback_selection_quiz_key_resp.getKeys({keyList: ['w', 'o'], waitRelease: false});
      _feedback_selection_quiz_key_resp_allKeys = _feedback_selection_quiz_key_resp_allKeys.concat(theseKeys);
      if (_feedback_selection_quiz_key_resp_allKeys.length > 0) {
        feedback_selection_quiz_key_resp.keys = _feedback_selection_quiz_key_resp_allKeys[_feedback_selection_quiz_key_resp_allKeys.length - 1].name;  // just the last key pressed
        feedback_selection_quiz_key_resp.rt = _feedback_selection_quiz_key_resp_allKeys[_feedback_selection_quiz_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedback_selection_quizComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function feedback_selection_quizRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'feedback_selection_quiz'-------
    for (const thisComponent of feedback_selection_quizComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    if (((feedback_selection_quiz_key_resp.keys === "o") && (select_feedback_to_press === 1))) {
        feedback_to_press_outcome = "correct";
        quiz_and_attention_check_fails = quiz_and_attention_check_fails;
    } else {
        if (((feedback_selection_quiz_key_resp.keys === "w") && (select_feedback_to_press === 1))) {
            feedback_to_press_outcome = "incorrect";
            quiz_and_attention_check_fails = (quiz_and_attention_check_fails + 1);
        } else {
            if (((feedback_selection_quiz_key_resp.keys === "o") && (select_feedback_to_press === 2))) {
                feedback_to_press_outcome = "incorrect";
                quiz_and_attention_check_fails = (quiz_and_attention_check_fails + 1);
            } else {
                if (((feedback_selection_quiz_key_resp.keys === "w") && (select_feedback_to_press === 2))) {
                    feedback_to_press_outcome = "correct";
                    quiz_and_attention_check_fails = quiz_and_attention_check_fails;
                }
            }
        }
    }
    select_feedback_to_press_slide.setAutoDraw(false);
    
    psychoJS.experiment.addData('feedback_selection_quiz_key_resp.keys', feedback_selection_quiz_key_resp.keys);
    if (typeof feedback_selection_quiz_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('feedback_selection_quiz_key_resp.rt', feedback_selection_quiz_key_resp.rt);
        routineTimer.reset();
        }
    
    feedback_selection_quiz_key_resp.stop();
    // the Routine "feedback_selection_quiz" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _feedback_post_quiz_reminder_key_resp_allKeys;
var feedback_post_quiz_reminderComponents;
function feedback_post_quiz_reminderRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'feedback_post_quiz_reminder'-------
    t = 0;
    feedback_post_quiz_reminderClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    if ((feedback_to_press_outcome === "correct")) {
        correct_feedback_reminder.setAutoDraw(true);
    } else {
        if ((feedback_to_press_outcome === "incorrect")) {
            incorrect_feedback_reminder.setAutoDraw(true);
        }
    }
    
    feedback_post_quiz_reminder_key_resp.keys = undefined;
    feedback_post_quiz_reminder_key_resp.rt = undefined;
    _feedback_post_quiz_reminder_key_resp_allKeys = [];
    // keep track of which components have finished
    feedback_post_quiz_reminderComponents = [];
    feedback_post_quiz_reminderComponents.push(feedback_post_quiz_reminder_key_resp);
    
    for (const thisComponent of feedback_post_quiz_reminderComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function feedback_post_quiz_reminderRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'feedback_post_quiz_reminder'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = feedback_post_quiz_reminderClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_post_quiz_reminder_key_resp* updates
    if (t >= 0.0 && feedback_post_quiz_reminder_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_post_quiz_reminder_key_resp.tStart = t;  // (not accounting for frame time here)
      feedback_post_quiz_reminder_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { feedback_post_quiz_reminder_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { feedback_post_quiz_reminder_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { feedback_post_quiz_reminder_key_resp.clearEvents(); });
    }

    if (feedback_post_quiz_reminder_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = feedback_post_quiz_reminder_key_resp.getKeys({keyList: [], waitRelease: false});
      _feedback_post_quiz_reminder_key_resp_allKeys = _feedback_post_quiz_reminder_key_resp_allKeys.concat(theseKeys);
      if (_feedback_post_quiz_reminder_key_resp_allKeys.length > 0) {
        feedback_post_quiz_reminder_key_resp.keys = _feedback_post_quiz_reminder_key_resp_allKeys[_feedback_post_quiz_reminder_key_resp_allKeys.length - 1].name;  // just the last key pressed
        feedback_post_quiz_reminder_key_resp.rt = _feedback_post_quiz_reminder_key_resp_allKeys[_feedback_post_quiz_reminder_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedback_post_quiz_reminderComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function feedback_post_quiz_reminderRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'feedback_post_quiz_reminder'-------
    for (const thisComponent of feedback_post_quiz_reminderComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    if ((feedback_to_press_outcome === "correct")) {
        correct_feedback_reminder.setAutoDraw(false);
    } else {
        if ((feedback_to_press_outcome === "incorrect")) {
            incorrect_feedback_reminder.setAutoDraw(false);
        }
    }
    psychoJS.experiment.addData("feedback_selection_quiz_result", feedback_to_press_outcome);
    
    psychoJS.experiment.addData('feedback_post_quiz_reminder_key_resp.keys', feedback_post_quiz_reminder_key_resp.keys);
    if (typeof feedback_post_quiz_reminder_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('feedback_post_quiz_reminder_key_resp.rt', feedback_post_quiz_reminder_key_resp.rt);
        routineTimer.reset();
        }
    
    feedback_post_quiz_reminder_key_resp.stop();
    // the Routine "feedback_post_quiz_reminder" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _slide_09_01_key_resp_allKeys;
var continue_slide_09_01Components;
function continue_slide_09_01RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'continue_slide_09_01'-------
    t = 0;
    continue_slide_09_01Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    instructions_slide_09_01.setAutoDraw(true);
    
    slide_09_01_key_resp.keys = undefined;
    slide_09_01_key_resp.rt = undefined;
    _slide_09_01_key_resp_allKeys = [];
    // keep track of which components have finished
    continue_slide_09_01Components = [];
    continue_slide_09_01Components.push(slide_09_01_key_resp);
    
    for (const thisComponent of continue_slide_09_01Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function continue_slide_09_01RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'continue_slide_09_01'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = continue_slide_09_01Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *slide_09_01_key_resp* updates
    if (t >= 0.0 && slide_09_01_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slide_09_01_key_resp.tStart = t;  // (not accounting for frame time here)
      slide_09_01_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { slide_09_01_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { slide_09_01_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { slide_09_01_key_resp.clearEvents(); });
    }

    if (slide_09_01_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = slide_09_01_key_resp.getKeys({keyList: [], waitRelease: false});
      _slide_09_01_key_resp_allKeys = _slide_09_01_key_resp_allKeys.concat(theseKeys);
      if (_slide_09_01_key_resp_allKeys.length > 0) {
        slide_09_01_key_resp.keys = _slide_09_01_key_resp_allKeys[_slide_09_01_key_resp_allKeys.length - 1].name;  // just the last key pressed
        slide_09_01_key_resp.rt = _slide_09_01_key_resp_allKeys[_slide_09_01_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of continue_slide_09_01Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function continue_slide_09_01RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'continue_slide_09_01'-------
    for (const thisComponent of continue_slide_09_01Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    instructions_slide_09_01.setAutoDraw(false);
    
    psychoJS.experiment.addData('slide_09_01_key_resp.keys', slide_09_01_key_resp.keys);
    if (typeof slide_09_01_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('slide_09_01_key_resp.rt', slide_09_01_key_resp.rt);
        routineTimer.reset();
        }
    
    slide_09_01_key_resp.stop();
    // the Routine "continue_slide_09_01" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _slide_09_02_key_resp_allKeys;
var continue_slide_09_02Components;
function continue_slide_09_02RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'continue_slide_09_02'-------
    t = 0;
    continue_slide_09_02Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    instructions_slide_09_02.setAutoDraw(true);
    
    slide_09_02_key_resp.keys = undefined;
    slide_09_02_key_resp.rt = undefined;
    _slide_09_02_key_resp_allKeys = [];
    // keep track of which components have finished
    continue_slide_09_02Components = [];
    continue_slide_09_02Components.push(slide_09_02_key_resp);
    
    for (const thisComponent of continue_slide_09_02Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function continue_slide_09_02RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'continue_slide_09_02'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = continue_slide_09_02Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *slide_09_02_key_resp* updates
    if (t >= 0.0 && slide_09_02_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slide_09_02_key_resp.tStart = t;  // (not accounting for frame time here)
      slide_09_02_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { slide_09_02_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { slide_09_02_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { slide_09_02_key_resp.clearEvents(); });
    }

    if (slide_09_02_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = slide_09_02_key_resp.getKeys({keyList: [], waitRelease: false});
      _slide_09_02_key_resp_allKeys = _slide_09_02_key_resp_allKeys.concat(theseKeys);
      if (_slide_09_02_key_resp_allKeys.length > 0) {
        slide_09_02_key_resp.keys = _slide_09_02_key_resp_allKeys[_slide_09_02_key_resp_allKeys.length - 1].name;  // just the last key pressed
        slide_09_02_key_resp.rt = _slide_09_02_key_resp_allKeys[_slide_09_02_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of continue_slide_09_02Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function continue_slide_09_02RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'continue_slide_09_02'-------
    for (const thisComponent of continue_slide_09_02Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    instructions_slide_09_02.setAutoDraw(false);
    
    psychoJS.experiment.addData('slide_09_02_key_resp.keys', slide_09_02_key_resp.keys);
    if (typeof slide_09_02_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('slide_09_02_key_resp.rt', slide_09_02_key_resp.rt);
        routineTimer.reset();
        }
    
    slide_09_02_key_resp.stop();
    // the Routine "continue_slide_09_02" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _slide_10_01_key_resp_allKeys;
var continue_slide_10_01Components;
function continue_slide_10_01RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'continue_slide_10_01'-------
    t = 0;
    continue_slide_10_01Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    instructions_slide_10_01.setAutoDraw(true);
    
    slide_10_01_key_resp.keys = undefined;
    slide_10_01_key_resp.rt = undefined;
    _slide_10_01_key_resp_allKeys = [];
    // keep track of which components have finished
    continue_slide_10_01Components = [];
    continue_slide_10_01Components.push(slide_10_01_key_resp);
    
    for (const thisComponent of continue_slide_10_01Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function continue_slide_10_01RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'continue_slide_10_01'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = continue_slide_10_01Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *slide_10_01_key_resp* updates
    if (t >= 0.0 && slide_10_01_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slide_10_01_key_resp.tStart = t;  // (not accounting for frame time here)
      slide_10_01_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { slide_10_01_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { slide_10_01_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { slide_10_01_key_resp.clearEvents(); });
    }

    if (slide_10_01_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = slide_10_01_key_resp.getKeys({keyList: [], waitRelease: false});
      _slide_10_01_key_resp_allKeys = _slide_10_01_key_resp_allKeys.concat(theseKeys);
      if (_slide_10_01_key_resp_allKeys.length > 0) {
        slide_10_01_key_resp.keys = _slide_10_01_key_resp_allKeys[_slide_10_01_key_resp_allKeys.length - 1].name;  // just the last key pressed
        slide_10_01_key_resp.rt = _slide_10_01_key_resp_allKeys[_slide_10_01_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of continue_slide_10_01Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function continue_slide_10_01RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'continue_slide_10_01'-------
    for (const thisComponent of continue_slide_10_01Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    instructions_slide_10_01.setAutoDraw(false);
    
    psychoJS.experiment.addData('slide_10_01_key_resp.keys', slide_10_01_key_resp.keys);
    if (typeof slide_10_01_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('slide_10_01_key_resp.rt', slide_10_01_key_resp.rt);
        routineTimer.reset();
        }
    
    slide_10_01_key_resp.stop();
    // the Routine "continue_slide_10_01" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _slide_10_02_key_resp_allKeys;
var continue_slide_10_02Components;
function continue_slide_10_02RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'continue_slide_10_02'-------
    t = 0;
    continue_slide_10_02Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    instructions_slide_10_02.setAutoDraw(true);
    
    slide_10_02_key_resp.keys = undefined;
    slide_10_02_key_resp.rt = undefined;
    _slide_10_02_key_resp_allKeys = [];
    // keep track of which components have finished
    continue_slide_10_02Components = [];
    continue_slide_10_02Components.push(slide_10_02_key_resp);
    
    for (const thisComponent of continue_slide_10_02Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function continue_slide_10_02RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'continue_slide_10_02'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = continue_slide_10_02Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *slide_10_02_key_resp* updates
    if (t >= 0.0 && slide_10_02_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slide_10_02_key_resp.tStart = t;  // (not accounting for frame time here)
      slide_10_02_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { slide_10_02_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { slide_10_02_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { slide_10_02_key_resp.clearEvents(); });
    }

    if (slide_10_02_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = slide_10_02_key_resp.getKeys({keyList: [], waitRelease: false});
      _slide_10_02_key_resp_allKeys = _slide_10_02_key_resp_allKeys.concat(theseKeys);
      if (_slide_10_02_key_resp_allKeys.length > 0) {
        slide_10_02_key_resp.keys = _slide_10_02_key_resp_allKeys[_slide_10_02_key_resp_allKeys.length - 1].name;  // just the last key pressed
        slide_10_02_key_resp.rt = _slide_10_02_key_resp_allKeys[_slide_10_02_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of continue_slide_10_02Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function continue_slide_10_02RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'continue_slide_10_02'-------
    for (const thisComponent of continue_slide_10_02Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    instructions_slide_10_02.setAutoDraw(false);
    
    psychoJS.experiment.addData('slide_10_02_key_resp.keys', slide_10_02_key_resp.keys);
    if (typeof slide_10_02_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('slide_10_02_key_resp.rt', slide_10_02_key_resp.rt);
        routineTimer.reset();
        }
    
    slide_10_02_key_resp.stop();
    // the Routine "continue_slide_10_02" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _get_shape_response_allKeys;
var attention_shape_checkComponents;
function attention_shape_checkRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'attention_shape_check'-------
    t = 0;
    attention_shape_checkClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    get_shape_response.keys = undefined;
    get_shape_response.rt = undefined;
    _get_shape_response_allKeys = [];
    // keep track of which components have finished
    attention_shape_checkComponents = [];
    attention_shape_checkComponents.push(get_shape_response);
    
    for (const thisComponent of attention_shape_checkComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function attention_shape_checkRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'attention_shape_check'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = attention_shape_checkClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    shapes_question.setAutoDraw(true);
    
    
    // *get_shape_response* updates
    if (t >= 0.0 && get_shape_response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      get_shape_response.tStart = t;  // (not accounting for frame time here)
      get_shape_response.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { get_shape_response.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { get_shape_response.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { get_shape_response.clearEvents(); });
    }

    if (get_shape_response.status === PsychoJS.Status.STARTED) {
      let theseKeys = get_shape_response.getKeys({keyList: ['1', '2'], waitRelease: false});
      _get_shape_response_allKeys = _get_shape_response_allKeys.concat(theseKeys);
      if (_get_shape_response_allKeys.length > 0) {
        get_shape_response.keys = _get_shape_response_allKeys[_get_shape_response_allKeys.length - 1].name;  // just the last key pressed
        get_shape_response.rt = _get_shape_response_allKeys[_get_shape_response_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of attention_shape_checkComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function attention_shape_checkRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'attention_shape_check'-------
    for (const thisComponent of attention_shape_checkComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    if ((get_shape_response.keys === "1")) {
        quiz_and_attention_check_fails = (quiz_and_attention_check_fails + 1);
        shape_quiz_result = "incorrect";
    } else {
        if ((get_shape_response.keys === "2")) {
            quiz_and_attention_check_fails = quiz_and_attention_check_fails;
            shape_quiz_result = "correct";
        }
    }
    shapes_question.setAutoDraw(false);
    
    psychoJS.experiment.addData('get_shape_response.keys', get_shape_response.keys);
    if (typeof get_shape_response.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('get_shape_response.rt', get_shape_response.rt);
        routineTimer.reset();
        }
    
    get_shape_response.stop();
    // the Routine "attention_shape_check" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _attention_reminder_key_resp_allKeys;
var attention_reminderComponents;
function attention_reminderRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'attention_reminder'-------
    t = 0;
    attention_reminderClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    attention_reminder_key_resp.keys = undefined;
    attention_reminder_key_resp.rt = undefined;
    _attention_reminder_key_resp_allKeys = [];
    if ((shape_quiz_result === "correct")) {
        correct_shape.setAutoDraw(true);
    } else {
        if ((shape_quiz_result === "incorrect")) {
            incorrect_shape.setAutoDraw(true);
        }
    }
    
    // keep track of which components have finished
    attention_reminderComponents = [];
    attention_reminderComponents.push(attention_reminder_key_resp);
    
    for (const thisComponent of attention_reminderComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function attention_reminderRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'attention_reminder'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = attention_reminderClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *attention_reminder_key_resp* updates
    if (t >= 0.0 && attention_reminder_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      attention_reminder_key_resp.tStart = t;  // (not accounting for frame time here)
      attention_reminder_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { attention_reminder_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { attention_reminder_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { attention_reminder_key_resp.clearEvents(); });
    }

    if (attention_reminder_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = attention_reminder_key_resp.getKeys({keyList: [], waitRelease: false});
      _attention_reminder_key_resp_allKeys = _attention_reminder_key_resp_allKeys.concat(theseKeys);
      if (_attention_reminder_key_resp_allKeys.length > 0) {
        attention_reminder_key_resp.keys = _attention_reminder_key_resp_allKeys[_attention_reminder_key_resp_allKeys.length - 1].name;  // just the last key pressed
        attention_reminder_key_resp.rt = _attention_reminder_key_resp_allKeys[_attention_reminder_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of attention_reminderComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function attention_reminderRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'attention_reminder'-------
    for (const thisComponent of attention_reminderComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('attention_reminder_key_resp.keys', attention_reminder_key_resp.keys);
    if (typeof attention_reminder_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('attention_reminder_key_resp.rt', attention_reminder_key_resp.rt);
        routineTimer.reset();
        }
    
    attention_reminder_key_resp.stop();
    if ((shape_quiz_result === "correct")) {
        correct_shape.setAutoDraw(false);
    } else {
        if ((shape_quiz_result === "incorrect")) {
            incorrect_shape.setAutoDraw(false);
        }
    }
    psychoJS.experiment.addData("shape_quiz_result", shape_quiz_result);
    
    // the Routine "attention_reminder" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _slide_11_key_resp_allKeys;
var continue_instructions_even_further_11Components;
function continue_instructions_even_further_11RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'continue_instructions_even_further_11'-------
    t = 0;
    continue_instructions_even_further_11Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    instructions_slide_eleven.setAutoDraw(true);
    
    slide_11_key_resp.keys = undefined;
    slide_11_key_resp.rt = undefined;
    _slide_11_key_resp_allKeys = [];
    // keep track of which components have finished
    continue_instructions_even_further_11Components = [];
    continue_instructions_even_further_11Components.push(slide_11_key_resp);
    
    for (const thisComponent of continue_instructions_even_further_11Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function continue_instructions_even_further_11RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'continue_instructions_even_further_11'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = continue_instructions_even_further_11Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *slide_11_key_resp* updates
    if (t >= 0.0 && slide_11_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slide_11_key_resp.tStart = t;  // (not accounting for frame time here)
      slide_11_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { slide_11_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { slide_11_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { slide_11_key_resp.clearEvents(); });
    }

    if (slide_11_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = slide_11_key_resp.getKeys({keyList: [], waitRelease: false});
      _slide_11_key_resp_allKeys = _slide_11_key_resp_allKeys.concat(theseKeys);
      if (_slide_11_key_resp_allKeys.length > 0) {
        slide_11_key_resp.keys = _slide_11_key_resp_allKeys[_slide_11_key_resp_allKeys.length - 1].name;  // just the last key pressed
        slide_11_key_resp.rt = _slide_11_key_resp_allKeys[_slide_11_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of continue_instructions_even_further_11Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function continue_instructions_even_further_11RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'continue_instructions_even_further_11'-------
    for (const thisComponent of continue_instructions_even_further_11Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    instructions_slide_eleven.setAutoDraw(false);
    
    psychoJS.experiment.addData('slide_11_key_resp.keys', slide_11_key_resp.keys);
    if (typeof slide_11_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('slide_11_key_resp.rt', slide_11_key_resp.rt);
        routineTimer.reset();
        }
    
    slide_11_key_resp.stop();
    // the Routine "continue_instructions_even_further_11" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _calib_one_space_allKeys;
var calib_oneComponents;
function calib_oneRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'calib_one'-------
    t = 0;
    calib_oneClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    calibration_slide_1.setAutoDraw(true);
    
    calib_one_space.keys = undefined;
    calib_one_space.rt = undefined;
    _calib_one_space_allKeys = [];
    // keep track of which components have finished
    calib_oneComponents = [];
    calib_oneComponents.push(calib_one_space);
    
    for (const thisComponent of calib_oneComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function calib_oneRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'calib_one'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = calib_oneClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *calib_one_space* updates
    if (t >= 0.0 && calib_one_space.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      calib_one_space.tStart = t;  // (not accounting for frame time here)
      calib_one_space.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { calib_one_space.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { calib_one_space.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { calib_one_space.clearEvents(); });
    }

    if (calib_one_space.status === PsychoJS.Status.STARTED) {
      let theseKeys = calib_one_space.getKeys({keyList: ['space'], waitRelease: false});
      _calib_one_space_allKeys = _calib_one_space_allKeys.concat(theseKeys);
      if (_calib_one_space_allKeys.length > 0) {
        calib_one_space.keys = _calib_one_space_allKeys[_calib_one_space_allKeys.length - 1].name;  // just the last key pressed
        calib_one_space.rt = _calib_one_space_allKeys[_calib_one_space_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of calib_oneComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function calib_oneRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'calib_one'-------
    for (const thisComponent of calib_oneComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    calibration_slide_1.setAutoDraw(false);
    
    psychoJS.experiment.addData('calib_one_space.keys', calib_one_space.keys);
    if (typeof calib_one_space.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('calib_one_space.rt', calib_one_space.rt);
        routineTimer.reset();
        }
    
    calib_one_space.stop();
    // the Routine "calib_one" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var calibration_update_duration;
var calibration_total_presses;
var slide_number;
var show_slide;
var calibration_time;
var time_of_calibration_press;
var time_of_calibration_press_list;
var _calibration_space_bar_press_allKeys;
var calib_lastComponents;
function calib_lastRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'calib_last'-------
    t = 0;
    calib_lastClock.reset(); // clock
    frameN = -1;
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    calibration_update_duration = 0.25;
    calibration_total_presses = 0;
    slide_number = 2;
    show_slide = new visual.ImageStim({"win": win, "image": (("calibration/slide" + slide_number.toString()) + ".png"), "size": [1, 0.75]});
    calibration_update_duration = 0.25;
    calibration_total_presses = 0;
    calibration_time = 3;
    time_of_calibration_press = [];
    time_of_calibration_press_list = [];
    
    calibration_space_bar_press.keys = undefined;
    calibration_space_bar_press.rt = undefined;
    _calibration_space_bar_press_allKeys = [];
    // keep track of which components have finished
    calib_lastComponents = [];
    calib_lastComponents.push(calibration_space_bar_press);
    
    for (const thisComponent of calib_lastComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var _pj;
var calib_keys;
function calib_lastRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'calib_last'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = calib_lastClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    show_slide = new visual.ImageStim({"win": win, "image": (("calibration/slide" + slide_number.toString()) + ".png"), "size": [1, 0.75]});
    show_slide.setAutoDraw(true);
    calib_keys = psychoJS.eventManager.getKeys();
    if (_pj.in_es6("space", calib_keys)) {
        time_of_calibration_press = calib_lastClock.getTime();
        time_of_calibration_press_list.push(time_of_calibration_press);
        calibration_total_presses = (calibration_total_presses + 1);
        if ((calib_lastClock.getTime() > calibration_update_duration)) {
            slide_number = (slide_number + 1);
            calibration_update_duration = (calibration_update_duration + 0.25);
        }
    }
    if ((calib_lastClock.getTime() > 3)) {
        show_slide.setAutoDraw(false);
    }
    
    
    // *calibration_space_bar_press* updates
    if (t >= 0.0 && calibration_space_bar_press.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      calibration_space_bar_press.tStart = t;  // (not accounting for frame time here)
      calibration_space_bar_press.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { calibration_space_bar_press.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { calibration_space_bar_press.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { calibration_space_bar_press.clearEvents(); });
    }

    frameRemains = 3.0  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (calibration_space_bar_press.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      calibration_space_bar_press.status = PsychoJS.Status.FINISHED;
  }

    if (calibration_space_bar_press.status === PsychoJS.Status.STARTED) {
      let theseKeys = calibration_space_bar_press.getKeys({keyList: ['space'], waitRelease: false});
      _calibration_space_bar_press_allKeys = _calibration_space_bar_press_allKeys.concat(theseKeys);
      if (_calibration_space_bar_press_allKeys.length > 0) {
        calibration_space_bar_press.keys = _calibration_space_bar_press_allKeys.map((key) => key.name);  // storing all keys
        calibration_space_bar_press.rt = _calibration_space_bar_press_allKeys.map((key) => key.rt);
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of calib_lastComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var maximum_work_for_feedback_threshold;
var work_for_feedback_threshold_multiplier;
var final_work_for_feedback_threshold;
function calib_lastRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'calib_last'-------
    for (const thisComponent of calib_lastComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    show_slide.setAutoDraw(false);
    blank_screen_image_black.setAutoDraw(true);
    maximum_work_for_feedback_threshold = (calibration_total_presses / calibration_time);
    work_for_feedback_threshold_multiplier = 0.9;
    final_work_for_feedback_threshold = (work_for_feedback_threshold_multiplier * maximum_work_for_feedback_threshold);
    psychoJS.experiment.addData("maximum_work_for_feedback_threshold", maximum_work_for_feedback_threshold);
    psychoJS.experiment.addData("final_work_for_feedback_threshold", final_work_for_feedback_threshold);
    
    psychoJS.experiment.addData('calibration_space_bar_press.keys', calibration_space_bar_press.keys);
    if (typeof calibration_space_bar_press.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('calibration_space_bar_press.rt', calibration_space_bar_press.rt);
        }
    
    calibration_space_bar_press.stop();
    return Scheduler.Event.NEXT;
  };
}


var _enter_to_practice_session_allKeys;
var advance_to_practice_sessionComponents;
function advance_to_practice_sessionRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'advance_to_practice_session'-------
    t = 0;
    advance_to_practice_sessionClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    enter_to_practice_session.keys = undefined;
    enter_to_practice_session.rt = undefined;
    _enter_to_practice_session_allKeys = [];
    instructions_slide_twelve.setAutoDraw(true);
    
    // keep track of which components have finished
    advance_to_practice_sessionComponents = [];
    advance_to_practice_sessionComponents.push(enter_to_practice_session);
    
    for (const thisComponent of advance_to_practice_sessionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function advance_to_practice_sessionRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'advance_to_practice_session'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = advance_to_practice_sessionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *enter_to_practice_session* updates
    if (t >= 0.0 && enter_to_practice_session.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enter_to_practice_session.tStart = t;  // (not accounting for frame time here)
      enter_to_practice_session.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { enter_to_practice_session.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { enter_to_practice_session.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { enter_to_practice_session.clearEvents(); });
    }

    if (enter_to_practice_session.status === PsychoJS.Status.STARTED) {
      let theseKeys = enter_to_practice_session.getKeys({keyList: ['return'], waitRelease: false});
      _enter_to_practice_session_allKeys = _enter_to_practice_session_allKeys.concat(theseKeys);
      if (_enter_to_practice_session_allKeys.length > 0) {
        enter_to_practice_session.keys = _enter_to_practice_session_allKeys[_enter_to_practice_session_allKeys.length - 1].name;  // just the last key pressed
        enter_to_practice_session.rt = _enter_to_practice_session_allKeys[_enter_to_practice_session_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of advance_to_practice_sessionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function advance_to_practice_sessionRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'advance_to_practice_session'-------
    for (const thisComponent of advance_to_practice_sessionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('enter_to_practice_session.keys', enter_to_practice_session.keys);
    if (typeof enter_to_practice_session.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('enter_to_practice_session.rt', enter_to_practice_session.rt);
        routineTimer.reset();
        }
    
    enter_to_practice_session.stop();
    instructions_slide_twelve.setAutoDraw(false);
    
    // the Routine "advance_to_practice_session" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var prac_trials;
var currentLoop;
function prac_trialsLoopBegin(prac_trialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  prac_trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: (("conditions/practice_task_option_" + excel_sheet_choice_practice) + ".xlsx"),
    seed: undefined, name: 'prac_trials'
  });
  psychoJS.experiment.addLoop(prac_trials); // add the loop to the experiment
  currentLoop = prac_trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisPrac_trial of prac_trials) {
    const snapshot = prac_trials.getSnapshot();
    prac_trialsLoopScheduler.add(importConditions(snapshot));
    prac_trialsLoopScheduler.add(practice_taskRoutineBegin(snapshot));
    prac_trialsLoopScheduler.add(practice_taskRoutineEachFrame(snapshot));
    prac_trialsLoopScheduler.add(practice_taskRoutineEnd(snapshot));
    prac_trialsLoopScheduler.add(isi_screenRoutineBegin(snapshot));
    prac_trialsLoopScheduler.add(isi_screenRoutineEachFrame(snapshot));
    prac_trialsLoopScheduler.add(isi_screenRoutineEnd(snapshot));
    const missed_trialLoopScheduler = new Scheduler(psychoJS);
    prac_trialsLoopScheduler.add(missed_trialLoopBegin, missed_trialLoopScheduler);
    prac_trialsLoopScheduler.add(missed_trialLoopScheduler);
    prac_trialsLoopScheduler.add(missed_trialLoopEnd);
    const no_feedback_work_trialLoopScheduler = new Scheduler(psychoJS);
    prac_trialsLoopScheduler.add(no_feedback_work_trialLoopBegin, no_feedback_work_trialLoopScheduler);
    prac_trialsLoopScheduler.add(no_feedback_work_trialLoopScheduler);
    prac_trialsLoopScheduler.add(no_feedback_work_trialLoopEnd);
    const feedback_work_trialLoopScheduler = new Scheduler(psychoJS);
    prac_trialsLoopScheduler.add(feedback_work_trialLoopBegin, feedback_work_trialLoopScheduler);
    prac_trialsLoopScheduler.add(feedback_work_trialLoopScheduler);
    prac_trialsLoopScheduler.add(feedback_work_trialLoopEnd);
    prac_trialsLoopScheduler.add(end_loop_data_logRoutineBegin(snapshot));
    prac_trialsLoopScheduler.add(end_loop_data_logRoutineEachFrame(snapshot));
    prac_trialsLoopScheduler.add(end_loop_data_logRoutineEnd(snapshot));
    prac_trialsLoopScheduler.add(endLoopIteration(prac_trialsLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


var missed_trial;
function missed_trialLoopBegin(missed_trialLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  missed_trial = new TrialHandler({
    psychoJS: psychoJS,
    nReps: draw_miss, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'missed_trial'
  });
  psychoJS.experiment.addLoop(missed_trial); // add the loop to the experiment
  currentLoop = missed_trial;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisMissed_trial of missed_trial) {
    const snapshot = missed_trial.getSnapshot();
    missed_trialLoopScheduler.add(importConditions(snapshot));
    missed_trialLoopScheduler.add(missed_trial_logicRoutineBegin(snapshot));
    missed_trialLoopScheduler.add(missed_trial_logicRoutineEachFrame(snapshot));
    missed_trialLoopScheduler.add(missed_trial_logicRoutineEnd(snapshot));
    missed_trialLoopScheduler.add(endLoopIteration(missed_trialLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function missed_trialLoopEnd() {
  psychoJS.experiment.removeLoop(missed_trial);

  return Scheduler.Event.NEXT;
}


var no_feedback_work_trial;
function no_feedback_work_trialLoopBegin(no_feedback_work_trialLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  no_feedback_work_trial = new TrialHandler({
    psychoJS: psychoJS,
    nReps: do_not_do_feedback, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'no_feedback_work_trial'
  });
  psychoJS.experiment.addLoop(no_feedback_work_trial); // add the loop to the experiment
  currentLoop = no_feedback_work_trial;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisNo_feedback_work_trial of no_feedback_work_trial) {
    const snapshot = no_feedback_work_trial.getSnapshot();
    no_feedback_work_trialLoopScheduler.add(importConditions(snapshot));
    no_feedback_work_trialLoopScheduler.add(no_feedback_work_logicRoutineBegin(snapshot));
    no_feedback_work_trialLoopScheduler.add(no_feedback_work_logicRoutineEachFrame(snapshot));
    no_feedback_work_trialLoopScheduler.add(no_feedback_work_logicRoutineEnd(snapshot));
    no_feedback_work_trialLoopScheduler.add(endLoopIteration(no_feedback_work_trialLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function no_feedback_work_trialLoopEnd() {
  psychoJS.experiment.removeLoop(no_feedback_work_trial);

  return Scheduler.Event.NEXT;
}


var feedback_work_trial;
function feedback_work_trialLoopBegin(feedback_work_trialLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  feedback_work_trial = new TrialHandler({
    psychoJS: psychoJS,
    nReps: do_feedback, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'feedback_work_trial'
  });
  psychoJS.experiment.addLoop(feedback_work_trial); // add the loop to the experiment
  currentLoop = feedback_work_trial;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisFeedback_work_trial of feedback_work_trial) {
    const snapshot = feedback_work_trial.getSnapshot();
    feedback_work_trialLoopScheduler.add(importConditions(snapshot));
    feedback_work_trialLoopScheduler.add(grey_work_for_fbRoutineBegin(snapshot));
    feedback_work_trialLoopScheduler.add(grey_work_for_fbRoutineEachFrame(snapshot));
    feedback_work_trialLoopScheduler.add(grey_work_for_fbRoutineEnd(snapshot));
    feedback_work_trialLoopScheduler.add(ask_want_to_work_for_feedbackRoutineBegin(snapshot));
    feedback_work_trialLoopScheduler.add(ask_want_to_work_for_feedbackRoutineEachFrame(snapshot));
    feedback_work_trialLoopScheduler.add(ask_want_to_work_for_feedbackRoutineEnd(snapshot));
    const no_loop_highlightLoopScheduler = new Scheduler(psychoJS);
    feedback_work_trialLoopScheduler.add(no_loop_highlightLoopBegin, no_loop_highlightLoopScheduler);
    feedback_work_trialLoopScheduler.add(no_loop_highlightLoopScheduler);
    feedback_work_trialLoopScheduler.add(no_loop_highlightLoopEnd);
    const yes_loop_highlightLoopScheduler = new Scheduler(psychoJS);
    feedback_work_trialLoopScheduler.add(yes_loop_highlightLoopBegin, yes_loop_highlightLoopScheduler);
    feedback_work_trialLoopScheduler.add(yes_loop_highlightLoopScheduler);
    feedback_work_trialLoopScheduler.add(yes_loop_highlightLoopEnd);
    feedback_work_trialLoopScheduler.add(endLoopIteration(feedback_work_trialLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


var no_loop_highlight;
function no_loop_highlightLoopBegin(no_loop_highlightLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  no_loop_highlight = new TrialHandler({
    psychoJS: psychoJS,
    nReps: highlight_no, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'no_loop_highlight'
  });
  psychoJS.experiment.addLoop(no_loop_highlight); // add the loop to the experiment
  currentLoop = no_loop_highlight;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisNo_loop_highlight of no_loop_highlight) {
    const snapshot = no_loop_highlight.getSnapshot();
    no_loop_highlightLoopScheduler.add(importConditions(snapshot));
    no_loop_highlightLoopScheduler.add(no_fb_highlightRoutineBegin(snapshot));
    no_loop_highlightLoopScheduler.add(no_fb_highlightRoutineEachFrame(snapshot));
    no_loop_highlightLoopScheduler.add(no_fb_highlightRoutineEnd(snapshot));
    no_loop_highlightLoopScheduler.add(endLoopIteration(no_loop_highlightLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function no_loop_highlightLoopEnd() {
  psychoJS.experiment.removeLoop(no_loop_highlight);

  return Scheduler.Event.NEXT;
}


var yes_loop_highlight;
function yes_loop_highlightLoopBegin(yes_loop_highlightLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  yes_loop_highlight = new TrialHandler({
    psychoJS: psychoJS,
    nReps: highlight_yes, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'yes_loop_highlight'
  });
  psychoJS.experiment.addLoop(yes_loop_highlight); // add the loop to the experiment
  currentLoop = yes_loop_highlight;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisYes_loop_highlight of yes_loop_highlight) {
    const snapshot = yes_loop_highlight.getSnapshot();
    yes_loop_highlightLoopScheduler.add(importConditions(snapshot));
    yes_loop_highlightLoopScheduler.add(yes_fb_highlightRoutineBegin(snapshot));
    yes_loop_highlightLoopScheduler.add(yes_fb_highlightRoutineEachFrame(snapshot));
    yes_loop_highlightLoopScheduler.add(yes_fb_highlightRoutineEnd(snapshot));
    yes_loop_highlightLoopScheduler.add(fb_work_timeRoutineBegin(snapshot));
    yes_loop_highlightLoopScheduler.add(fb_work_timeRoutineEachFrame(snapshot));
    yes_loop_highlightLoopScheduler.add(fb_work_timeRoutineEnd(snapshot));
    yes_loop_highlightLoopScheduler.add(draw_feedback_to_screenRoutineBegin(snapshot));
    yes_loop_highlightLoopScheduler.add(draw_feedback_to_screenRoutineEachFrame(snapshot));
    yes_loop_highlightLoopScheduler.add(draw_feedback_to_screenRoutineEnd(snapshot));
    yes_loop_highlightLoopScheduler.add(post_work_blankRoutineBegin(snapshot));
    yes_loop_highlightLoopScheduler.add(post_work_blankRoutineEachFrame(snapshot));
    yes_loop_highlightLoopScheduler.add(post_work_blankRoutineEnd(snapshot));
    yes_loop_highlightLoopScheduler.add(endLoopIteration(yes_loop_highlightLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function yes_loop_highlightLoopEnd() {
  psychoJS.experiment.removeLoop(yes_loop_highlight);

  return Scheduler.Event.NEXT;
}


function feedback_work_trialLoopEnd() {
  psychoJS.experiment.removeLoop(feedback_work_trial);

  return Scheduler.Event.NEXT;
}


function prac_trialsLoopEnd() {
  psychoJS.experiment.removeLoop(prac_trials);

  return Scheduler.Event.NEXT;
}


var main_trials;
function main_trialsLoopBegin(main_trialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  main_trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: (("conditions/main_task_option_" + excel_sheet_choice_main) + ".xlsx"),
    seed: undefined, name: 'main_trials'
  });
  psychoJS.experiment.addLoop(main_trials); // add the loop to the experiment
  currentLoop = main_trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisMain_trial of main_trials) {
    const snapshot = main_trials.getSnapshot();
    main_trialsLoopScheduler.add(importConditions(snapshot));
    main_trialsLoopScheduler.add(main_taskRoutineBegin(snapshot));
    main_trialsLoopScheduler.add(main_taskRoutineEachFrame(snapshot));
    main_trialsLoopScheduler.add(main_taskRoutineEnd(snapshot));
    main_trialsLoopScheduler.add(isi_screenRoutineBegin(snapshot));
    main_trialsLoopScheduler.add(isi_screenRoutineEachFrame(snapshot));
    main_trialsLoopScheduler.add(isi_screenRoutineEnd(snapshot));
    const missed_trial_main_taskLoopScheduler = new Scheduler(psychoJS);
    main_trialsLoopScheduler.add(missed_trial_main_taskLoopBegin, missed_trial_main_taskLoopScheduler);
    main_trialsLoopScheduler.add(missed_trial_main_taskLoopScheduler);
    main_trialsLoopScheduler.add(missed_trial_main_taskLoopEnd);
    const no_feedback_work_trial_mainLoopScheduler = new Scheduler(psychoJS);
    main_trialsLoopScheduler.add(no_feedback_work_trial_mainLoopBegin, no_feedback_work_trial_mainLoopScheduler);
    main_trialsLoopScheduler.add(no_feedback_work_trial_mainLoopScheduler);
    main_trialsLoopScheduler.add(no_feedback_work_trial_mainLoopEnd);
    const feedback_work_trial_mainLoopScheduler = new Scheduler(psychoJS);
    main_trialsLoopScheduler.add(feedback_work_trial_mainLoopBegin, feedback_work_trial_mainLoopScheduler);
    main_trialsLoopScheduler.add(feedback_work_trial_mainLoopScheduler);
    main_trialsLoopScheduler.add(feedback_work_trial_mainLoopEnd);
    main_trialsLoopScheduler.add(end_loop_data_logRoutineBegin(snapshot));
    main_trialsLoopScheduler.add(end_loop_data_logRoutineEachFrame(snapshot));
    main_trialsLoopScheduler.add(end_loop_data_logRoutineEnd(snapshot));
    main_trialsLoopScheduler.add(endLoopIteration(main_trialsLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


var missed_trial_main_task;
function missed_trial_main_taskLoopBegin(missed_trial_main_taskLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  missed_trial_main_task = new TrialHandler({
    psychoJS: psychoJS,
    nReps: draw_miss, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'missed_trial_main_task'
  });
  psychoJS.experiment.addLoop(missed_trial_main_task); // add the loop to the experiment
  currentLoop = missed_trial_main_task;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisMissed_trial_main_task of missed_trial_main_task) {
    const snapshot = missed_trial_main_task.getSnapshot();
    missed_trial_main_taskLoopScheduler.add(importConditions(snapshot));
    missed_trial_main_taskLoopScheduler.add(missed_trial_logicRoutineBegin(snapshot));
    missed_trial_main_taskLoopScheduler.add(missed_trial_logicRoutineEachFrame(snapshot));
    missed_trial_main_taskLoopScheduler.add(missed_trial_logicRoutineEnd(snapshot));
    missed_trial_main_taskLoopScheduler.add(endLoopIteration(missed_trial_main_taskLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function missed_trial_main_taskLoopEnd() {
  psychoJS.experiment.removeLoop(missed_trial_main_task);

  return Scheduler.Event.NEXT;
}


var no_feedback_work_trial_main;
function no_feedback_work_trial_mainLoopBegin(no_feedback_work_trial_mainLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  no_feedback_work_trial_main = new TrialHandler({
    psychoJS: psychoJS,
    nReps: do_not_do_feedback, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'no_feedback_work_trial_main'
  });
  psychoJS.experiment.addLoop(no_feedback_work_trial_main); // add the loop to the experiment
  currentLoop = no_feedback_work_trial_main;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisNo_feedback_work_trial_main of no_feedback_work_trial_main) {
    const snapshot = no_feedback_work_trial_main.getSnapshot();
    no_feedback_work_trial_mainLoopScheduler.add(importConditions(snapshot));
    no_feedback_work_trial_mainLoopScheduler.add(no_feedback_work_logicRoutineBegin(snapshot));
    no_feedback_work_trial_mainLoopScheduler.add(no_feedback_work_logicRoutineEachFrame(snapshot));
    no_feedback_work_trial_mainLoopScheduler.add(no_feedback_work_logicRoutineEnd(snapshot));
    no_feedback_work_trial_mainLoopScheduler.add(endLoopIteration(no_feedback_work_trial_mainLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function no_feedback_work_trial_mainLoopEnd() {
  psychoJS.experiment.removeLoop(no_feedback_work_trial_main);

  return Scheduler.Event.NEXT;
}


var feedback_work_trial_main;
function feedback_work_trial_mainLoopBegin(feedback_work_trial_mainLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  feedback_work_trial_main = new TrialHandler({
    psychoJS: psychoJS,
    nReps: do_feedback, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'feedback_work_trial_main'
  });
  psychoJS.experiment.addLoop(feedback_work_trial_main); // add the loop to the experiment
  currentLoop = feedback_work_trial_main;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisFeedback_work_trial_main of feedback_work_trial_main) {
    const snapshot = feedback_work_trial_main.getSnapshot();
    feedback_work_trial_mainLoopScheduler.add(importConditions(snapshot));
    feedback_work_trial_mainLoopScheduler.add(grey_work_for_fbRoutineBegin(snapshot));
    feedback_work_trial_mainLoopScheduler.add(grey_work_for_fbRoutineEachFrame(snapshot));
    feedback_work_trial_mainLoopScheduler.add(grey_work_for_fbRoutineEnd(snapshot));
    feedback_work_trial_mainLoopScheduler.add(ask_want_to_work_for_feedbackRoutineBegin(snapshot));
    feedback_work_trial_mainLoopScheduler.add(ask_want_to_work_for_feedbackRoutineEachFrame(snapshot));
    feedback_work_trial_mainLoopScheduler.add(ask_want_to_work_for_feedbackRoutineEnd(snapshot));
    const no_loop_highlight_mainLoopScheduler = new Scheduler(psychoJS);
    feedback_work_trial_mainLoopScheduler.add(no_loop_highlight_mainLoopBegin, no_loop_highlight_mainLoopScheduler);
    feedback_work_trial_mainLoopScheduler.add(no_loop_highlight_mainLoopScheduler);
    feedback_work_trial_mainLoopScheduler.add(no_loop_highlight_mainLoopEnd);
    const yes_loop_highlight_mainLoopScheduler = new Scheduler(psychoJS);
    feedback_work_trial_mainLoopScheduler.add(yes_loop_highlight_mainLoopBegin, yes_loop_highlight_mainLoopScheduler);
    feedback_work_trial_mainLoopScheduler.add(yes_loop_highlight_mainLoopScheduler);
    feedback_work_trial_mainLoopScheduler.add(yes_loop_highlight_mainLoopEnd);
    feedback_work_trial_mainLoopScheduler.add(endLoopIteration(feedback_work_trial_mainLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


var no_loop_highlight_main;
function no_loop_highlight_mainLoopBegin(no_loop_highlight_mainLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  no_loop_highlight_main = new TrialHandler({
    psychoJS: psychoJS,
    nReps: highlight_no, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'no_loop_highlight_main'
  });
  psychoJS.experiment.addLoop(no_loop_highlight_main); // add the loop to the experiment
  currentLoop = no_loop_highlight_main;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisNo_loop_highlight_main of no_loop_highlight_main) {
    const snapshot = no_loop_highlight_main.getSnapshot();
    no_loop_highlight_mainLoopScheduler.add(importConditions(snapshot));
    no_loop_highlight_mainLoopScheduler.add(no_fb_highlightRoutineBegin(snapshot));
    no_loop_highlight_mainLoopScheduler.add(no_fb_highlightRoutineEachFrame(snapshot));
    no_loop_highlight_mainLoopScheduler.add(no_fb_highlightRoutineEnd(snapshot));
    no_loop_highlight_mainLoopScheduler.add(endLoopIteration(no_loop_highlight_mainLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function no_loop_highlight_mainLoopEnd() {
  psychoJS.experiment.removeLoop(no_loop_highlight_main);

  return Scheduler.Event.NEXT;
}


var yes_loop_highlight_main;
function yes_loop_highlight_mainLoopBegin(yes_loop_highlight_mainLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  yes_loop_highlight_main = new TrialHandler({
    psychoJS: psychoJS,
    nReps: highlight_yes, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'yes_loop_highlight_main'
  });
  psychoJS.experiment.addLoop(yes_loop_highlight_main); // add the loop to the experiment
  currentLoop = yes_loop_highlight_main;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisYes_loop_highlight_main of yes_loop_highlight_main) {
    const snapshot = yes_loop_highlight_main.getSnapshot();
    yes_loop_highlight_mainLoopScheduler.add(importConditions(snapshot));
    yes_loop_highlight_mainLoopScheduler.add(yes_fb_highlightRoutineBegin(snapshot));
    yes_loop_highlight_mainLoopScheduler.add(yes_fb_highlightRoutineEachFrame(snapshot));
    yes_loop_highlight_mainLoopScheduler.add(yes_fb_highlightRoutineEnd(snapshot));
    yes_loop_highlight_mainLoopScheduler.add(fb_work_timeRoutineBegin(snapshot));
    yes_loop_highlight_mainLoopScheduler.add(fb_work_timeRoutineEachFrame(snapshot));
    yes_loop_highlight_mainLoopScheduler.add(fb_work_timeRoutineEnd(snapshot));
    yes_loop_highlight_mainLoopScheduler.add(draw_feedback_to_screenRoutineBegin(snapshot));
    yes_loop_highlight_mainLoopScheduler.add(draw_feedback_to_screenRoutineEachFrame(snapshot));
    yes_loop_highlight_mainLoopScheduler.add(draw_feedback_to_screenRoutineEnd(snapshot));
    yes_loop_highlight_mainLoopScheduler.add(post_work_blankRoutineBegin(snapshot));
    yes_loop_highlight_mainLoopScheduler.add(post_work_blankRoutineEachFrame(snapshot));
    yes_loop_highlight_mainLoopScheduler.add(post_work_blankRoutineEnd(snapshot));
    yes_loop_highlight_mainLoopScheduler.add(endLoopIteration(yes_loop_highlight_mainLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function yes_loop_highlight_mainLoopEnd() {
  psychoJS.experiment.removeLoop(yes_loop_highlight_main);

  return Scheduler.Event.NEXT;
}


function feedback_work_trial_mainLoopEnd() {
  psychoJS.experiment.removeLoop(feedback_work_trial_main);

  return Scheduler.Event.NEXT;
}


function main_trialsLoopEnd() {
  psychoJS.experiment.removeLoop(main_trials);

  return Scheduler.Event.NEXT;
}


var work_total_presses;
var _key_resp_prac_allKeys;
var decision_to_work_for_feedback;
var time_of_press_list;
var current_work_rate_list;
var current_opacity_level_list;
var final_opacity_level;
var practice_taskComponents;
function practice_taskRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'practice_task'-------
    t = 0;
    practice_taskClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    work_total_presses = 0;
    prac_trial_num = (prac_trial_num + 1);
    psychoJS.experiment.addData("mode", "practice");
    psychoJS.experiment.addData("prac_trial_num", prac_trial_num);
    psychoJS.experiment.addData("calibration_total_presses", calibration_total_presses);
    psychoJS.experiment.addData("maximum_work_for_feedback_threshold", maximum_work_for_feedback_threshold);
    psychoJS.experiment.addData("final_work_for_feedback_threshold", final_work_for_feedback_threshold);
    
    fractal_one_prac.setPos([fractal_60_x_pos, fractal_60_y_pos]);
    fractal_one_prac.setImage(fractal_60_stim);
    fractal_two_prac.setPos([fractal_80_x_pos, fractal_80_y_pos]);
    fractal_two_prac.setImage(fractal_80_stim);
    key_resp_prac.keys = undefined;
    key_resp_prac.rt = undefined;
    _key_resp_prac_allKeys = [];
    decision_to_work_for_feedback = [];
    time_of_press_list = [];
    current_work_rate_list = [];
    current_opacity_level_list = [];
    final_opacity_level = [];
    
    // keep track of which components have finished
    practice_taskComponents = [];
    practice_taskComponents.push(iti_prac);
    practice_taskComponents.push(fractal_one_prac);
    practice_taskComponents.push(fractal_two_prac);
    practice_taskComponents.push(key_resp_prac);
    
    for (const thisComponent of practice_taskComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function practice_taskRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'practice_task'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = practice_taskClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *iti_prac* updates
    if (t >= 0.0 && iti_prac.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      iti_prac.tStart = t;  // (not accounting for frame time here)
      iti_prac.frameNStart = frameN;  // exact frame index
      
      iti_prac.setAutoDraw(true);
    }

    frameRemains = 0.0 + iti - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (iti_prac.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      iti_prac.setAutoDraw(false);
    }
    
    // *fractal_one_prac* updates
    if (((iti_prac.status == FINISHED)) && fractal_one_prac.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fractal_one_prac.tStart = t;  // (not accounting for frame time here)
      fractal_one_prac.frameNStart = frameN;  // exact frame index
      
      fractal_one_prac.setAutoDraw(true);
    }

    if (fractal_one_prac.status === PsychoJS.Status.STARTED && t >= (fractal_one_prac.tStart + 2.0)) {
      fractal_one_prac.setAutoDraw(false);
    }
    
    // *fractal_two_prac* updates
    if (((iti_prac.status == FINISHED)) && fractal_two_prac.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fractal_two_prac.tStart = t;  // (not accounting for frame time here)
      fractal_two_prac.frameNStart = frameN;  // exact frame index
      
      fractal_two_prac.setAutoDraw(true);
    }

    if (fractal_two_prac.status === PsychoJS.Status.STARTED && t >= (fractal_two_prac.tStart + 2.0)) {
      fractal_two_prac.setAutoDraw(false);
    }
    
    // *key_resp_prac* updates
    if (((iti_prac.status == FINISHED)) && key_resp_prac.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_prac.tStart = t;  // (not accounting for frame time here)
      key_resp_prac.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_prac.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_prac.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_prac.clearEvents(); });
    }

    if (key_resp_prac.status === PsychoJS.Status.STARTED && t >= (key_resp_prac.tStart + 2.0)) {
      key_resp_prac.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp_prac.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_prac.getKeys({keyList: ['f', 'j'], waitRelease: false});
      _key_resp_prac_allKeys = _key_resp_prac_allKeys.concat(theseKeys);
      if (_key_resp_prac_allKeys.length > 0) {
        key_resp_prac.keys = _key_resp_prac_allKeys[_key_resp_prac_allKeys.length - 1].name;  // just the last key pressed
        key_resp_prac.rt = _key_resp_prac_allKeys[_key_resp_prac_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practice_taskComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var outcome;
var side_chosen;
var fractal_chosen;
var reward;
var load_feedback_stim_to_draw;
var do_not_do_feedback;
var do_feedback;
var draw_miss;
function practice_taskRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'practice_task'-------
    for (const thisComponent of practice_taskComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp_prac.keys', key_resp_prac.keys);
    if (typeof key_resp_prac.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_prac.rt', key_resp_prac.rt);
        routineTimer.reset();
        }
    
    key_resp_prac.stop();
    outcome = [];
    side_chosen = [];
    fractal_chosen = [];
    reward = [];
    if ((condition === 1)) {
        if ((((key_resp_prac.keys === "f") && (fractal_60_side === "left")) && (fractal_60_reward === 1))) {
            outcome = "good";
            side_chosen = "left";
            fractal_chosen = "fractal_60";
            reward = 1;
            prac_total_points = (prac_total_points + 1);
        } else {
            if ((((key_resp_prac.keys === "f") && (fractal_60_side === "left")) && (fractal_60_reward === 0))) {
                outcome = "bad";
                side_chosen = "left";
                fractal_chosen = "fractal_60";
                reward = 0;
                prac_total_points = prac_total_points;
            } else {
                if ((((key_resp_prac.keys === "j") && (fractal_60_side === "right")) && (fractal_60_reward === 1))) {
                    outcome = "good";
                    side_chosen = "right";
                    fractal_chosen = "fractal_60";
                    reward = 1;
                    prac_total_points = (prac_total_points + 1);
                } else {
                    if ((((key_resp_prac.keys === "j") && (fractal_60_side === "right")) && (fractal_60_reward === 0))) {
                        outcome = "bad";
                        side_chosen = "right";
                        fractal_chosen = "fractal_60";
                        reward = 0;
                        prac_total_points = prac_total_points;
                    } else {
                        if ((((key_resp_prac.keys === "f") && (fractal_80_side === "left")) && (fractal_80_reward === 1))) {
                            outcome = "good";
                            side_chosen = "left";
                            fractal_chosen = "fractal_80";
                            reward = 1;
                            prac_total_points = (prac_total_points + 1);
                        } else {
                            if ((((key_resp_prac.keys === "f") && (fractal_80_side === "left")) && (fractal_80_reward === 0))) {
                                outcome = "bad";
                                side_chosen = "left";
                                fractal_chosen = "fractal_80";
                                reward = 0;
                                prac_total_points = prac_total_points;
                            } else {
                                if ((((key_resp_prac.keys === "j") && (fractal_80_side === "right")) && (fractal_80_reward === 1))) {
                                    outcome = "good";
                                    side_chosen = "right";
                                    fractal_chosen = "fractal_80";
                                    reward = 1;
                                    prac_total_points = (prac_total_points + 1);
                                } else {
                                    if ((((key_resp_prac.keys === "j") && (fractal_80_side === "right")) && (fractal_80_reward === 0))) {
                                        outcome = "bad";
                                        side_chosen = "right";
                                        fractal_chosen = "fractal_80";
                                        reward = 0;
                                        prac_total_points = prac_total_points;
                                    } else {
                                        outcome = "missed";
                                        side_chosen = "n/a";
                                        fractal_chosen = "n/a";
                                        reward = 0;
                                        prac_total_points = prac_total_points;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    } else {
        if ((condition === 2)) {
            if ((((key_resp_prac.keys === "f") && (fractal_60_side === "left")) && (fractal_60_reward === 1))) {
                outcome = "good";
                side_chosen = "left";
                fractal_chosen = "fractal_60";
                reward = 1;
                prac_total_points = (prac_total_points + 1);
            } else {
                if ((((key_resp_prac.keys === "f") && (fractal_60_side === "left")) && (fractal_60_reward === 0))) {
                    outcome = "bad";
                    side_chosen = "left";
                    fractal_chosen = "fractal_60";
                    reward = 0;
                    prac_total_points = prac_total_points;
                } else {
                    if ((((key_resp_prac.keys === "j") && (fractal_60_side === "right")) && (fractal_60_reward === 1))) {
                        outcome = "good";
                        side_chosen = "right";
                        fractal_chosen = "fractal_60";
                        reward = 1;
                        prac_total_points = (prac_total_points + 1);
                    } else {
                        if ((((key_resp_prac.keys === "j") && (fractal_60_side === "right")) && (fractal_60_reward === 0))) {
                            outcome = "bad";
                            side_chosen = "right";
                            fractal_chosen = "fractal_60";
                            reward = 0;
                            prac_total_points = prac_total_points;
                        } else {
                            if ((((key_resp_prac.keys === "f") && (fractal_80_side === "left")) && (fractal_80_reward === 1))) {
                                outcome = "good";
                                side_chosen = "left";
                                fractal_chosen = "fractal_80";
                                reward = 1;
                                prac_total_points = (prac_total_points + 1);
                            } else {
                                if ((((key_resp_prac.keys === "f") && (fractal_80_side === "left")) && (fractal_80_reward === 0))) {
                                    outcome = "bad";
                                    side_chosen = "left";
                                    fractal_chosen = "fractal_80";
                                    reward = 0;
                                    prac_total_points = prac_total_points;
                                } else {
                                    if ((((key_resp_prac.keys === "j") && (fractal_80_side === "right")) && (fractal_80_reward === 1))) {
                                        outcome = "good";
                                        side_chosen = "right";
                                        fractal_chosen = "fractal_80";
                                        reward = 1;
                                        prac_total_points = (prac_total_points + 1);
                                    } else {
                                        if ((((key_resp_prac.keys === "j") && (fractal_80_side === "right")) && (fractal_80_reward === 0))) {
                                            outcome = "bad";
                                            side_chosen = "right";
                                            fractal_chosen = "fractal_80";
                                            reward = 0;
                                            prac_total_points = prac_total_points;
                                        } else {
                                            outcome = "missed";
                                            side_chosen = "n/a";
                                            fractal_chosen = "n/a";
                                            reward = 0;
                                            prac_total_points = prac_total_points;
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    psychoJS.experiment.addData("side_chosen", side_chosen);
    psychoJS.experiment.addData("fractal_chosen", fractal_chosen);
    psychoJS.experiment.addData("reward", reward);
    psychoJS.experiment.addData("total_points", prac_total_points);
    
    load_feedback_stim_to_draw = [];
    if ((((feedback_outcome === "veridical_feedback") && (outcome === "good")) && (condition === 1))) {
        decision_to_work_for_feedback = "n/a";
        load_feedback_stim_to_draw = vertical_feedback_stim;
    } else {
        if ((((feedback_outcome === "veridical_feedback") && (outcome === "bad")) && (condition === 1))) {
            decision_to_work_for_feedback = "n/a";
            load_feedback_stim_to_draw = horizontal_feedback_stim;
        } else {
            if ((((feedback_outcome === "veridical_feedback") && (outcome === "good")) && (condition === 2))) {
                decision_to_work_for_feedback = "n/a";
                load_feedback_stim_to_draw = horizontal_feedback_stim;
            } else {
                if ((((feedback_outcome === "veridical_feedback") && (outcome === "bad")) && (condition === 2))) {
                    decision_to_work_for_feedback = "n/a";
                    load_feedback_stim_to_draw = vertical_feedback_stim;
                } else {
                    if ((outcome === "missed")) {
                        decision_to_work_for_feedback = "missed_trial";
                    } else {
                        if ((feedback_outcome === "no_feedback")) {
                            decision_to_work_for_feedback = "n/a";
                            load_feedback_stim_to_draw = grey_no_feedback_stim;
                        } else {
                            if ((feedback_outcome === "work_option")) {
                                decision_to_work_for_feedback = "probe";
                                load_feedback_stim_to_draw = grey_no_feedback_stim;
                            }
                        }
                    }
                }
            }
        }
    }
    do_not_do_feedback = [];
    do_feedback = [];
    if ((decision_to_work_for_feedback === "n/a")) {
        do_not_do_feedback = 1;
        do_feedback = 0;
        draw_miss = 0;
    } else {
        if ((decision_to_work_for_feedback === "probe")) {
            do_not_do_feedback = 0;
            do_feedback = 1;
            draw_miss = 0;
        } else {
            if ((decision_to_work_for_feedback === "missed_trial")) {
                do_not_do_feedback = 0;
                do_feedback = 0;
                draw_miss = 1;
            }
        }
    }
    
    // the Routine "practice_task" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var isi_screenComponents;
function isi_screenRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'isi_screen'-------
    t = 0;
    isi_screenClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // keep track of which components have finished
    isi_screenComponents = [];
    isi_screenComponents.push(isi_stim);
    
    for (const thisComponent of isi_screenComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function isi_screenRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'isi_screen'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = isi_screenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *isi_stim* updates
    if (t >= 0.0 && isi_stim.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      isi_stim.tStart = t;  // (not accounting for frame time here)
      isi_stim.frameNStart = frameN;  // exact frame index
      
      isi_stim.setAutoDraw(true);
    }

    frameRemains = 0.0 + isi - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (isi_stim.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      isi_stim.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of isi_screenComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function isi_screenRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'isi_screen'-------
    for (const thisComponent of isi_screenComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "isi_screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var missed_trial_logicComponents;
function missed_trial_logicRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'missed_trial_logic'-------
    t = 0;
    missed_trial_logicClock.reset(); // clock
    frameN = -1;
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    missed_trial_logicComponents = [];
    missed_trial_logicComponents.push(missed_trial_practice);
    
    for (const thisComponent of missed_trial_logicComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function missed_trial_logicRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'missed_trial_logic'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = missed_trial_logicClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *missed_trial_practice* updates
    if (t >= 0.0 && missed_trial_practice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      missed_trial_practice.tStart = t;  // (not accounting for frame time here)
      missed_trial_practice.frameNStart = frameN;  // exact frame index
      
      missed_trial_practice.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (missed_trial_practice.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      missed_trial_practice.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of missed_trial_logicComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function missed_trial_logicRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'missed_trial_logic'-------
    for (const thisComponent of missed_trial_logicComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var no_feedback_work_logicComponents;
function no_feedback_work_logicRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'no_feedback_work_logic'-------
    t = 0;
    no_feedback_work_logicClock.reset(); // clock
    frameN = -1;
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    load_feedback_stim_to_draw.pos = [0, 0];
    load_feedback_stim_to_draw.setAutoDraw(true);
    
    // keep track of which components have finished
    no_feedback_work_logicComponents = [];
    no_feedback_work_logicComponents.push(no_feedback_work_image);
    
    for (const thisComponent of no_feedback_work_logicComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function no_feedback_work_logicRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'no_feedback_work_logic'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = no_feedback_work_logicClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *no_feedback_work_image* updates
    if (t >= 0.0 && no_feedback_work_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      no_feedback_work_image.tStart = t;  // (not accounting for frame time here)
      no_feedback_work_image.frameNStart = frameN;  // exact frame index
      
      no_feedback_work_image.setAutoDraw(true);
    }

    frameRemains = 2.0  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (no_feedback_work_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      no_feedback_work_image.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of no_feedback_work_logicComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function no_feedback_work_logicRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'no_feedback_work_logic'-------
    for (const thisComponent of no_feedback_work_logicComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    load_feedback_stim_to_draw.pos = [0, 0];
    load_feedback_stim_to_draw.setAutoDraw(false);
    
    return Scheduler.Event.NEXT;
  };
}


var grey_work_for_fbComponents;
function grey_work_for_fbRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'grey_work_for_fb'-------
    t = 0;
    grey_work_for_fbClock.reset(); // clock
    frameN = -1;
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    load_feedback_stim_to_draw.pos = [0, 0];
    load_feedback_stim_to_draw.setAutoDraw(true);
    
    // keep track of which components have finished
    grey_work_for_fbComponents = [];
    grey_work_for_fbComponents.push(grey_stim_work_for_fb);
    
    for (const thisComponent of grey_work_for_fbComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function grey_work_for_fbRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'grey_work_for_fb'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = grey_work_for_fbClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *grey_stim_work_for_fb* updates
    if (t >= 0.0 && grey_stim_work_for_fb.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      grey_stim_work_for_fb.tStart = t;  // (not accounting for frame time here)
      grey_stim_work_for_fb.frameNStart = frameN;  // exact frame index
      
      grey_stim_work_for_fb.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (grey_stim_work_for_fb.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      grey_stim_work_for_fb.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of grey_work_for_fbComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function grey_work_for_fbRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'grey_work_for_fb'-------
    for (const thisComponent of grey_work_for_fbComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    load_feedback_stim_to_draw.pos = [0, 0];
    load_feedback_stim_to_draw.setAutoDraw(false);
    
    return Scheduler.Event.NEXT;
  };
}


var _feedback_choice_key_resp_allKeys;
var ask_want_to_work_for_feedbackComponents;
function ask_want_to_work_for_feedbackRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'ask_want_to_work_for_feedback'-------
    t = 0;
    ask_want_to_work_for_feedbackClock.reset(); // clock
    frameN = -1;
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    feedback_choice_key_resp.keys = undefined;
    feedback_choice_key_resp.rt = undefined;
    _feedback_choice_key_resp_allKeys = [];
    // keep track of which components have finished
    ask_want_to_work_for_feedbackComponents = [];
    ask_want_to_work_for_feedbackComponents.push(feedback_choice_key_resp);
    ask_want_to_work_for_feedbackComponents.push(feedback_choice_slide);
    
    for (const thisComponent of ask_want_to_work_for_feedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function ask_want_to_work_for_feedbackRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'ask_want_to_work_for_feedback'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = ask_want_to_work_for_feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_choice_key_resp* updates
    if (t >= 0.0 && feedback_choice_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_choice_key_resp.tStart = t;  // (not accounting for frame time here)
      feedback_choice_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { feedback_choice_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { feedback_choice_key_resp.start(); }); // start on screen flip
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (feedback_choice_key_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback_choice_key_resp.status = PsychoJS.Status.FINISHED;
  }

    if (feedback_choice_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = feedback_choice_key_resp.getKeys({keyList: ['o', 'w'], waitRelease: false});
      _feedback_choice_key_resp_allKeys = _feedback_choice_key_resp_allKeys.concat(theseKeys);
      if (_feedback_choice_key_resp_allKeys.length > 0) {
        feedback_choice_key_resp.keys = _feedback_choice_key_resp_allKeys[_feedback_choice_key_resp_allKeys.length - 1].name;  // just the last key pressed
        feedback_choice_key_resp.rt = _feedback_choice_key_resp_allKeys[_feedback_choice_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *feedback_choice_slide* updates
    if (t >= 0.0 && feedback_choice_slide.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_choice_slide.tStart = t;  // (not accounting for frame time here)
      feedback_choice_slide.frameNStart = frameN;  // exact frame index
      
      feedback_choice_slide.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (feedback_choice_slide.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback_choice_slide.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ask_want_to_work_for_feedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var highlight_no;
var highlight_yes;
function ask_want_to_work_for_feedbackRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'ask_want_to_work_for_feedback'-------
    for (const thisComponent of ask_want_to_work_for_feedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('feedback_choice_key_resp.keys', feedback_choice_key_resp.keys);
    if (typeof feedback_choice_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('feedback_choice_key_resp.rt', feedback_choice_key_resp.rt);
        routineTimer.reset();
        }
    
    feedback_choice_key_resp.stop();
    highlight_no = [];
    highlight_yes = [];
    if ((feedback_choice_key_resp.keys === "w")) {
        decision_to_work_for_feedback = "yes";
        highlight_no = 0;
        highlight_yes = 1;
    } else {
        if ((feedback_choice_key_resp.keys === "o")) {
            decision_to_work_for_feedback = "no";
            highlight_no = 1;
            highlight_yes = 0;
        } else {
            decision_to_work_for_feedback = "missed";
            highlight_no = 0;
            highlight_yes = 0;
        }
    }
    
    return Scheduler.Event.NEXT;
  };
}


var no_fb_highlightComponents;
function no_fb_highlightRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'no_fb_highlight'-------
    t = 0;
    no_fb_highlightClock.reset(); // clock
    frameN = -1;
    routineTimer.add(0.300000);
    // update component parameters for each repeat
    // keep track of which components have finished
    no_fb_highlightComponents = [];
    no_fb_highlightComponents.push(no_fb_slide);
    
    for (const thisComponent of no_fb_highlightComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function no_fb_highlightRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'no_fb_highlight'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = no_fb_highlightClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *no_fb_slide* updates
    if (t >= 0.0 && no_fb_slide.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      no_fb_slide.tStart = t;  // (not accounting for frame time here)
      no_fb_slide.frameNStart = frameN;  // exact frame index
      
      no_fb_slide.setAutoDraw(true);
    }

    frameRemains = 0.3  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (no_fb_slide.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      no_fb_slide.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of no_fb_highlightComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function no_fb_highlightRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'no_fb_highlight'-------
    for (const thisComponent of no_fb_highlightComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var yes_fb_highlightComponents;
function yes_fb_highlightRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'yes_fb_highlight'-------
    t = 0;
    yes_fb_highlightClock.reset(); // clock
    frameN = -1;
    routineTimer.add(0.300000);
    // update component parameters for each repeat
    // keep track of which components have finished
    yes_fb_highlightComponents = [];
    yes_fb_highlightComponents.push(yes_fb_slide);
    
    for (const thisComponent of yes_fb_highlightComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function yes_fb_highlightRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'yes_fb_highlight'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = yes_fb_highlightClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *yes_fb_slide* updates
    if (t >= 0.0 && yes_fb_slide.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      yes_fb_slide.tStart = t;  // (not accounting for frame time here)
      yes_fb_slide.frameNStart = frameN;  // exact frame index
      
      yes_fb_slide.setAutoDraw(true);
    }

    frameRemains = 0.3  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (yes_fb_slide.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      yes_fb_slide.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of yes_fb_highlightComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function yes_fb_highlightRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'yes_fb_highlight'-------
    for (const thisComponent of yes_fb_highlightComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var feedback_stim_to_draw;
var fb_work_timeComponents;
function fb_work_timeRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'fb_work_time'-------
    t = 0;
    fb_work_timeClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    feedback_stim_to_draw = [];
    if ((condition === 1)) {
        if ((outcome === "good")) {
            feedback_stim_to_draw = vertical_feedback_stim;
        } else {
            if ((outcome === "bad")) {
                feedback_stim_to_draw = horizontal_feedback_stim;
            }
        }
    } else {
        if ((condition === 2)) {
            if ((outcome === "good")) {
                feedback_stim_to_draw = horizontal_feedback_stim;
            } else {
                if ((outcome === "bad")) {
                    feedback_stim_to_draw = vertical_feedback_stim;
                }
            }
        }
    }
    
    // keep track of which components have finished
    fb_work_timeComponents = [];
    
    for (const thisComponent of fb_work_timeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function fb_work_timeRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'fb_work_time'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = fb_work_timeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of fb_work_timeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fb_work_timeRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'fb_work_time'-------
    for (const thisComponent of fb_work_timeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "fb_work_time" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var update_opacity;
var time_of_press;
var current_work_rate;
var _work_for_feedback_space_bar_press_allKeys;
var draw_feedback_to_screenComponents;
function draw_feedback_to_screenRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'draw_feedback_to_screen'-------
    t = 0;
    draw_feedback_to_screenClock.reset(); // clock
    frameN = -1;
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    feedback_stim_to_draw.pos = [0, 0];
    grey_no_feedback_stim.pos = [0, 0];
    feedback_stim_to_draw.opacity = 1;
    grey_no_feedback_stim.opacity = 1;
    update_opacity = 0.015;
    time_of_press = [];
    time_of_press_list = [];
    work_total_presses = 0;
    current_work_rate = [];
    current_work_rate_list = [];
    current_opacity_level_list = [];
    final_opacity_level = [];
    event.clearEvents();
    
    work_for_feedback_space_bar_press.keys = undefined;
    work_for_feedback_space_bar_press.rt = undefined;
    _work_for_feedback_space_bar_press_allKeys = [];
    // keep track of which components have finished
    draw_feedback_to_screenComponents = [];
    draw_feedback_to_screenComponents.push(work_for_feedback_space_bar_press);
    
    for (const thisComponent of draw_feedback_to_screenComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var keys;
function draw_feedback_to_screenRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'draw_feedback_to_screen'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = draw_feedback_to_screenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    feedback_stim_to_draw.setAutoDraw(true);
    grey_no_feedback_stim.setAutoDraw(true);
    keys = psychoJS.eventManager.getKeys();
    if ((_pj.in_es6("space", keys) && (draw_feedback_to_screenClock.getTime() < 3.0))) {
        time_of_press = draw_feedback_to_screenClock.getTime();
        time_of_press_list.push(time_of_press);
        work_total_presses = (work_total_presses + 1);
        current_work_rate = (work_total_presses / time_of_press);
        current_opacity_level_list.push(grey_no_feedback_stim.opacity);
        if ((current_work_rate > final_work_for_feedback_threshold)) {
            grey_no_feedback_stim.opacity = (grey_no_feedback_stim.opacity - update_opacity);
        }
    }
    
    
    // *work_for_feedback_space_bar_press* updates
    if (t >= 0.0 && work_for_feedback_space_bar_press.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      work_for_feedback_space_bar_press.tStart = t;  // (not accounting for frame time here)
      work_for_feedback_space_bar_press.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { work_for_feedback_space_bar_press.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { work_for_feedback_space_bar_press.start(); }); // start on screen flip
    }

    frameRemains = 3.0  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (work_for_feedback_space_bar_press.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      work_for_feedback_space_bar_press.status = PsychoJS.Status.FINISHED;
  }

    if (work_for_feedback_space_bar_press.status === PsychoJS.Status.STARTED) {
      let theseKeys = work_for_feedback_space_bar_press.getKeys({keyList: ['e'], waitRelease: false});
      _work_for_feedback_space_bar_press_allKeys = _work_for_feedback_space_bar_press_allKeys.concat(theseKeys);
      if (_work_for_feedback_space_bar_press_allKeys.length > 0) {
        work_for_feedback_space_bar_press.keys = _work_for_feedback_space_bar_press_allKeys[_work_for_feedback_space_bar_press_allKeys.length - 1].name;  // just the last key pressed
        work_for_feedback_space_bar_press.rt = _work_for_feedback_space_bar_press_allKeys[_work_for_feedback_space_bar_press_allKeys.length - 1].rt;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of draw_feedback_to_screenComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function draw_feedback_to_screenRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'draw_feedback_to_screen'-------
    for (const thisComponent of draw_feedback_to_screenComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    feedback_stim_to_draw.setAutoDraw(false);
    grey_no_feedback_stim.setAutoDraw(false);
    final_opacity_level = grey_no_feedback_stim.opacity;
    event.clearEvents();
    
    return Scheduler.Event.NEXT;
  };
}


var _post_work_space_presses_allKeys;
var post_work_blankComponents;
function post_work_blankRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'post_work_blank'-------
    t = 0;
    post_work_blankClock.reset(); // clock
    frameN = -1;
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    post_work_space_presses.keys = undefined;
    post_work_space_presses.rt = undefined;
    _post_work_space_presses_allKeys = [];
    // keep track of which components have finished
    post_work_blankComponents = [];
    post_work_blankComponents.push(blank_image);
    post_work_blankComponents.push(post_work_space_presses);
    
    for (const thisComponent of post_work_blankComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function post_work_blankRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'post_work_blank'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = post_work_blankClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *blank_image* updates
    if (t >= 0.0 && blank_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blank_image.tStart = t;  // (not accounting for frame time here)
      blank_image.frameNStart = frameN;  // exact frame index
      
      blank_image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (blank_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      blank_image.setAutoDraw(false);
    }
    
    // *post_work_space_presses* updates
    if (t >= 0.0 && post_work_space_presses.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      post_work_space_presses.tStart = t;  // (not accounting for frame time here)
      post_work_space_presses.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { post_work_space_presses.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { post_work_space_presses.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { post_work_space_presses.clearEvents(); });
    }

    frameRemains = 1.0  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (post_work_space_presses.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      post_work_space_presses.status = PsychoJS.Status.FINISHED;
  }

    if (post_work_space_presses.status === PsychoJS.Status.STARTED) {
      let theseKeys = post_work_space_presses.getKeys({keyList: ['space'], waitRelease: false});
      _post_work_space_presses_allKeys = _post_work_space_presses_allKeys.concat(theseKeys);
      if (_post_work_space_presses_allKeys.length > 0) {
        post_work_space_presses.keys = _post_work_space_presses_allKeys.map((key) => key.name);  // storing all keys
        post_work_space_presses.rt = _post_work_space_presses_allKeys.map((key) => key.rt);
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of post_work_blankComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function post_work_blankRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'post_work_blank'-------
    for (const thisComponent of post_work_blankComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('post_work_space_presses.keys', post_work_space_presses.keys);
    if (typeof post_work_space_presses.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('post_work_space_presses.rt', post_work_space_presses.rt);
        }
    
    post_work_space_presses.stop();
    return Scheduler.Event.NEXT;
  };
}


var end_loop_data_logComponents;
function end_loop_data_logRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'end_loop_data_log'-------
    t = 0;
    end_loop_data_logClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // keep track of which components have finished
    end_loop_data_logComponents = [];
    
    for (const thisComponent of end_loop_data_logComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function end_loop_data_logRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'end_loop_data_log'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = end_loop_data_logClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of end_loop_data_logComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function end_loop_data_logRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'end_loop_data_log'-------
    for (const thisComponent of end_loop_data_logComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData("decision_to_work_for_feedback", decision_to_work_for_feedback);
    psychoJS.experiment.addData("time_of_press_list", time_of_press_list);
    psychoJS.experiment.addData("work_total_presses", work_total_presses);
    psychoJS.experiment.addData("current_work_rate_list", current_work_rate_list);
    psychoJS.experiment.addData("current_opacity_level_list", current_opacity_level_list);
    psychoJS.experiment.addData("final_opacity_level", final_opacity_level);
    
    // the Routine "end_loop_data_log" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var blank_screen_2Components;
function blank_screen_2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'blank_screen_2'-------
    t = 0;
    blank_screen_2Clock.reset(); // clock
    frameN = -1;
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    blank_screen_2Components = [];
    blank_screen_2Components.push(blank_slide_2);
    
    for (const thisComponent of blank_screen_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function blank_screen_2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'blank_screen_2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = blank_screen_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *blank_slide_2* updates
    if (t >= 0.0 && blank_slide_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blank_slide_2.tStart = t;  // (not accounting for frame time here)
      blank_slide_2.frameNStart = frameN;  // exact frame index
      
      blank_slide_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (blank_slide_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      blank_slide_2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of blank_screen_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function blank_screen_2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'blank_screen_2'-------
    for (const thisComponent of blank_screen_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _start_second_quiz_allKeys;
var second_quizComponents;
function second_quizRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'second_quiz'-------
    t = 0;
    second_quizClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    instructions_slide_thirteen.setAutoDraw(true);
    
    start_second_quiz.keys = undefined;
    start_second_quiz.rt = undefined;
    _start_second_quiz_allKeys = [];
    // keep track of which components have finished
    second_quizComponents = [];
    second_quizComponents.push(start_second_quiz);
    
    for (const thisComponent of second_quizComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function second_quizRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'second_quiz'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = second_quizClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *start_second_quiz* updates
    if (t >= 0.0 && start_second_quiz.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      start_second_quiz.tStart = t;  // (not accounting for frame time here)
      start_second_quiz.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { start_second_quiz.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { start_second_quiz.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { start_second_quiz.clearEvents(); });
    }

    if (start_second_quiz.status === PsychoJS.Status.STARTED) {
      let theseKeys = start_second_quiz.getKeys({keyList: [], waitRelease: false});
      _start_second_quiz_allKeys = _start_second_quiz_allKeys.concat(theseKeys);
      if (_start_second_quiz_allKeys.length > 0) {
        start_second_quiz.keys = _start_second_quiz_allKeys[_start_second_quiz_allKeys.length - 1].name;  // just the last key pressed
        start_second_quiz.rt = _start_second_quiz_allKeys[_start_second_quiz_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of second_quizComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function second_quizRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'second_quiz'-------
    for (const thisComponent of second_quizComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    instructions_slide_thirteen.setAutoDraw(false);
    
    psychoJS.experiment.addData('start_second_quiz.keys', start_second_quiz.keys);
    if (typeof start_second_quiz.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('start_second_quiz.rt', start_second_quiz.rt);
        routineTimer.reset();
        }
    
    start_second_quiz.stop();
    // the Routine "second_quiz" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _first_q_second_quiz_resp_allKeys;
var second_quiz_first_questionComponents;
function second_quiz_first_questionRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'second_quiz_first_question'-------
    t = 0;
    second_quiz_first_questionClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    grey_no_feedback_stim.pos = [0, 0.12];
    grey_no_feedback_stim.size = [0.1, 0.1];
    instructions_slide_six.setAutoDraw(true);
    grey_no_feedback_stim.setAutoDraw(true);
    
    first_q_second_quiz_resp.keys = undefined;
    first_q_second_quiz_resp.rt = undefined;
    _first_q_second_quiz_resp_allKeys = [];
    // keep track of which components have finished
    second_quiz_first_questionComponents = [];
    second_quiz_first_questionComponents.push(first_q_second_quiz_resp);
    
    for (const thisComponent of second_quiz_first_questionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function second_quiz_first_questionRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'second_quiz_first_question'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = second_quiz_first_questionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *first_q_second_quiz_resp* updates
    if (t >= 0.0 && first_q_second_quiz_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      first_q_second_quiz_resp.tStart = t;  // (not accounting for frame time here)
      first_q_second_quiz_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { first_q_second_quiz_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { first_q_second_quiz_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { first_q_second_quiz_resp.clearEvents(); });
    }

    if (first_q_second_quiz_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = first_q_second_quiz_resp.getKeys({keyList: ['1', '2', '3'], waitRelease: false});
      _first_q_second_quiz_resp_allKeys = _first_q_second_quiz_resp_allKeys.concat(theseKeys);
      if (_first_q_second_quiz_resp_allKeys.length > 0) {
        first_q_second_quiz_resp.keys = _first_q_second_quiz_resp_allKeys[_first_q_second_quiz_resp_allKeys.length - 1].name;  // just the last key pressed
        first_q_second_quiz_resp.rt = _first_q_second_quiz_resp_allKeys[_first_q_second_quiz_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of second_quiz_first_questionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function second_quiz_first_questionRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'second_quiz_first_question'-------
    for (const thisComponent of second_quiz_first_questionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    if ((first_q_second_quiz_resp.keys === "1")) {
        quiz_and_attention_check_fails = (quiz_and_attention_check_fails + 1);
        second_stim_quiz_first_question_result = "incorrect";
    } else {
        if ((first_q_second_quiz_resp.keys === "2")) {
            quiz_and_attention_check_fails = (quiz_and_attention_check_fails + 1);
            second_stim_quiz_first_question_result = "incorrect";
        } else {
            if ((first_q_second_quiz_resp.keys === "3")) {
                quiz_and_attention_check_fails = quiz_and_attention_check_fails;
                second_stim_quiz_first_question_result = "correct";
            }
        }
    }
    grey_no_feedback_stim.pos = [0, 0.12];
    grey_no_feedback_stim.size = [0.1, 0.1];
    instructions_slide_six.setAutoDraw(false);
    grey_no_feedback_stim.setAutoDraw(false);
    
    psychoJS.experiment.addData('first_q_second_quiz_resp.keys', first_q_second_quiz_resp.keys);
    if (typeof first_q_second_quiz_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('first_q_second_quiz_resp.rt', first_q_second_quiz_resp.rt);
        routineTimer.reset();
        }
    
    first_q_second_quiz_resp.stop();
    // the Routine "second_quiz_first_question" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _advance_q_2_quiz_2_allKeys;
var second_quiz_first_question_reminderComponents;
function second_quiz_first_question_reminderRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'second_quiz_first_question_reminder'-------
    t = 0;
    second_quiz_first_question_reminderClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    if ((second_stim_quiz_first_question_result === "correct")) {
        grey_no_feedback_stim.pos = [0, 0.12];
        grey_no_feedback_stim.size = [0.1, 0.1];
        correct_result_no_feedback.setAutoDraw(true);
        grey_no_feedback_stim.setAutoDraw(true);
    } else {
        if ((second_stim_quiz_first_question_result === "incorrect")) {
            grey_no_feedback_stim.pos = [0, 0.12];
            grey_no_feedback_stim.size = [0.1, 0.1];
            incorrect_result_no_feedback.setAutoDraw(true);
            grey_no_feedback_stim.setAutoDraw(true);
        }
    }
    
    advance_q_2_quiz_2.keys = undefined;
    advance_q_2_quiz_2.rt = undefined;
    _advance_q_2_quiz_2_allKeys = [];
    // keep track of which components have finished
    second_quiz_first_question_reminderComponents = [];
    second_quiz_first_question_reminderComponents.push(advance_q_2_quiz_2);
    
    for (const thisComponent of second_quiz_first_question_reminderComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function second_quiz_first_question_reminderRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'second_quiz_first_question_reminder'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = second_quiz_first_question_reminderClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *advance_q_2_quiz_2* updates
    if (t >= 0.0 && advance_q_2_quiz_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      advance_q_2_quiz_2.tStart = t;  // (not accounting for frame time here)
      advance_q_2_quiz_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { advance_q_2_quiz_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { advance_q_2_quiz_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { advance_q_2_quiz_2.clearEvents(); });
    }

    if (advance_q_2_quiz_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = advance_q_2_quiz_2.getKeys({keyList: [], waitRelease: false});
      _advance_q_2_quiz_2_allKeys = _advance_q_2_quiz_2_allKeys.concat(theseKeys);
      if (_advance_q_2_quiz_2_allKeys.length > 0) {
        advance_q_2_quiz_2.keys = _advance_q_2_quiz_2_allKeys[_advance_q_2_quiz_2_allKeys.length - 1].name;  // just the last key pressed
        advance_q_2_quiz_2.rt = _advance_q_2_quiz_2_allKeys[_advance_q_2_quiz_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of second_quiz_first_question_reminderComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function second_quiz_first_question_reminderRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'second_quiz_first_question_reminder'-------
    for (const thisComponent of second_quiz_first_question_reminderComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    if ((second_stim_quiz_first_question_result === "correct")) {
        grey_no_feedback_stim.pos = [0, 0.12];
        grey_no_feedback_stim.size = [0.1, 0.1];
        correct_result_no_feedback.setAutoDraw(false);
        grey_no_feedback_stim.setAutoDraw(false);
    } else {
        if ((second_stim_quiz_first_question_result === "incorrect")) {
            grey_no_feedback_stim.pos = [0, 0.12];
            grey_no_feedback_stim.size = [0.1, 0.1];
            incorrect_result_no_feedback.setAutoDraw(false);
            grey_no_feedback_stim.setAutoDraw(false);
        }
    }
    
    psychoJS.experiment.addData('advance_q_2_quiz_2.keys', advance_q_2_quiz_2.keys);
    if (typeof advance_q_2_quiz_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('advance_q_2_quiz_2.rt', advance_q_2_quiz_2.rt);
        routineTimer.reset();
        }
    
    advance_q_2_quiz_2.stop();
    // the Routine "second_quiz_first_question_reminder" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _resp_q_2_q_2_allKeys;
var second_quiz_second_questionComponents;
function second_quiz_second_questionRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'second_quiz_second_question'-------
    t = 0;
    second_quiz_second_questionClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    vertical_feedback_stim.pos = [0, 0.12];
    vertical_feedback_stim.size = [0.1, 0.1];
    instructions_slide_six.setAutoDraw(true);
    vertical_feedback_stim.setAutoDraw(true);
    
    resp_q_2_q_2.keys = undefined;
    resp_q_2_q_2.rt = undefined;
    _resp_q_2_q_2_allKeys = [];
    // keep track of which components have finished
    second_quiz_second_questionComponents = [];
    second_quiz_second_questionComponents.push(resp_q_2_q_2);
    
    for (const thisComponent of second_quiz_second_questionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function second_quiz_second_questionRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'second_quiz_second_question'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = second_quiz_second_questionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *resp_q_2_q_2* updates
    if (t >= 0.0 && resp_q_2_q_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp_q_2_q_2.tStart = t;  // (not accounting for frame time here)
      resp_q_2_q_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp_q_2_q_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp_q_2_q_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp_q_2_q_2.clearEvents(); });
    }

    if (resp_q_2_q_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp_q_2_q_2.getKeys({keyList: ['1', '2', '3'], waitRelease: false});
      _resp_q_2_q_2_allKeys = _resp_q_2_q_2_allKeys.concat(theseKeys);
      if (_resp_q_2_q_2_allKeys.length > 0) {
        resp_q_2_q_2.keys = _resp_q_2_q_2_allKeys[_resp_q_2_q_2_allKeys.length - 1].name;  // just the last key pressed
        resp_q_2_q_2.rt = _resp_q_2_q_2_allKeys[_resp_q_2_q_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of second_quiz_second_questionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function second_quiz_second_questionRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'second_quiz_second_question'-------
    for (const thisComponent of second_quiz_second_questionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    if (((resp_q_2_q_2.keys === "1") && (condition === 1))) {
        quiz_and_attention_check_fails = quiz_and_attention_check_fails;
        second_stim_quiz_second_question_result = "correct";
    } else {
        if (((resp_q_2_q_2.keys === "2") && (condition === 1))) {
            quiz_and_attention_check_fails = (quiz_and_attention_check_fails + 1);
            second_stim_quiz_second_question_result = "incorrect";
        } else {
            if (((resp_q_2_q_2.keys === "3") && (condition === 1))) {
                quiz_and_attention_check_fails = (quiz_and_attention_check_fails + 1);
                second_stim_quiz_second_question_result = "incorrect";
            } else {
                if (((resp_q_2_q_2.keys === "1") && (condition === 2))) {
                    quiz_and_attention_check_fails = (quiz_and_attention_check_fails + 1);
                    second_stim_quiz_second_question_result = "incorrect";
                } else {
                    if (((resp_q_2_q_2.keys === "2") && (condition === 2))) {
                        quiz_and_attention_check_fails = quiz_and_attention_check_fails;
                        second_stim_quiz_second_question_result = "correct";
                    } else {
                        if (((resp_q_2_q_2.keys === "3") && (condition === 2))) {
                            quiz_and_attention_check_fails = (quiz_and_attention_check_fails + 1);
                            second_stim_quiz_second_question_result = "incorrect";
                        }
                    }
                }
            }
        }
    }
    vertical_feedback_stim.pos = [0, 0.12];
    vertical_feedback_stim.size = [0.1, 0.1];
    instructions_slide_six.setAutoDraw(false);
    vertical_feedback_stim.setAutoDraw(false);
    
    psychoJS.experiment.addData('resp_q_2_q_2.keys', resp_q_2_q_2.keys);
    if (typeof resp_q_2_q_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp_q_2_q_2.rt', resp_q_2_q_2.rt);
        routineTimer.reset();
        }
    
    resp_q_2_q_2.stop();
    // the Routine "second_quiz_second_question" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _advance_q_3_quiz_2_allKeys;
var second_quiz_second_question_reminderComponents;
function second_quiz_second_question_reminderRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'second_quiz_second_question_reminder'-------
    t = 0;
    second_quiz_second_question_reminderClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    if (((second_stim_quiz_second_question_result === "correct") && (condition === 1))) {
        vertical_feedback_stim.pos = [0, 0.12];
        vertical_feedback_stim.size = [0.1, 0.1];
        correct_result_plus_one.setAutoDraw(true);
        vertical_feedback_stim.setAutoDraw(true);
    } else {
        if (((second_stim_quiz_second_question_result === "incorrect") && (condition === 1))) {
            vertical_feedback_stim.pos = [0, 0.12];
            vertical_feedback_stim.size = [0.1, 0.1];
            incorrect_result_plus_one.setAutoDraw(true);
            vertical_feedback_stim.setAutoDraw(true);
        } else {
            if (((second_stim_quiz_second_question_result === "correct") && (condition === 2))) {
                vertical_feedback_stim.pos = [0, 0.12];
                vertical_feedback_stim.size = [0.1, 0.1];
                correct_result_plus_zero.setAutoDraw(true);
                vertical_feedback_stim.setAutoDraw(true);
            } else {
                if (((second_stim_quiz_second_question_result === "incorrect") && (condition === 2))) {
                    vertical_feedback_stim.pos = [0, 0.12];
                    vertical_feedback_stim.size = [0.1, 0.1];
                    incorrect_result_plus_zero.setAutoDraw(true);
                    vertical_feedback_stim.setAutoDraw(true);
                }
            }
        }
    }
    
    advance_q_3_quiz_2.keys = undefined;
    advance_q_3_quiz_2.rt = undefined;
    _advance_q_3_quiz_2_allKeys = [];
    // keep track of which components have finished
    second_quiz_second_question_reminderComponents = [];
    second_quiz_second_question_reminderComponents.push(advance_q_3_quiz_2);
    
    for (const thisComponent of second_quiz_second_question_reminderComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function second_quiz_second_question_reminderRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'second_quiz_second_question_reminder'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = second_quiz_second_question_reminderClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *advance_q_3_quiz_2* updates
    if (t >= 0.0 && advance_q_3_quiz_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      advance_q_3_quiz_2.tStart = t;  // (not accounting for frame time here)
      advance_q_3_quiz_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { advance_q_3_quiz_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { advance_q_3_quiz_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { advance_q_3_quiz_2.clearEvents(); });
    }

    if (advance_q_3_quiz_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = advance_q_3_quiz_2.getKeys({keyList: [], waitRelease: false});
      _advance_q_3_quiz_2_allKeys = _advance_q_3_quiz_2_allKeys.concat(theseKeys);
      if (_advance_q_3_quiz_2_allKeys.length > 0) {
        advance_q_3_quiz_2.keys = _advance_q_3_quiz_2_allKeys[_advance_q_3_quiz_2_allKeys.length - 1].name;  // just the last key pressed
        advance_q_3_quiz_2.rt = _advance_q_3_quiz_2_allKeys[_advance_q_3_quiz_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of second_quiz_second_question_reminderComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function second_quiz_second_question_reminderRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'second_quiz_second_question_reminder'-------
    for (const thisComponent of second_quiz_second_question_reminderComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    if (((second_stim_quiz_second_question_result === "correct") && (condition === 1))) {
        vertical_feedback_stim.pos = [0, 0.12];
        vertical_feedback_stim.size = [0.1, 0.1];
        correct_result_plus_one.setAutoDraw(false);
        vertical_feedback_stim.setAutoDraw(false);
    } else {
        if (((second_stim_quiz_second_question_result === "incorrect") && (condition === 1))) {
            vertical_feedback_stim.pos = [0, 0.12];
            vertical_feedback_stim.size = [0.1, 0.1];
            incorrect_result_plus_one.setAutoDraw(false);
            vertical_feedback_stim.setAutoDraw(false);
        } else {
            if (((second_stim_quiz_second_question_result === "correct") && (condition === 2))) {
                vertical_feedback_stim.pos = [0, 0.12];
                vertical_feedback_stim.size = [0.1, 0.1];
                correct_result_plus_zero.setAutoDraw(false);
                vertical_feedback_stim.setAutoDraw(false);
            } else {
                if (((second_stim_quiz_second_question_result === "incorrect") && (condition === 2))) {
                    vertical_feedback_stim.pos = [0, 0.12];
                    vertical_feedback_stim.size = [0.1, 0.1];
                    incorrect_result_plus_zero.setAutoDraw(false);
                    vertical_feedback_stim.setAutoDraw(false);
                }
            }
        }
    }
    
    psychoJS.experiment.addData('advance_q_3_quiz_2.keys', advance_q_3_quiz_2.keys);
    if (typeof advance_q_3_quiz_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('advance_q_3_quiz_2.rt', advance_q_3_quiz_2.rt);
        routineTimer.reset();
        }
    
    advance_q_3_quiz_2.stop();
    // the Routine "second_quiz_second_question_reminder" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _resp_quiz_2_q_3_allKeys;
var second_quiz_third_questionComponents;
function second_quiz_third_questionRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'second_quiz_third_question'-------
    t = 0;
    second_quiz_third_questionClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    horizontal_feedback_stim.pos = [0, 0.12];
    horizontal_feedback_stim.size = [0.1, 0.1];
    instructions_slide_six.setAutoDraw(true);
    horizontal_feedback_stim.setAutoDraw(true);
    
    resp_quiz_2_q_3.keys = undefined;
    resp_quiz_2_q_3.rt = undefined;
    _resp_quiz_2_q_3_allKeys = [];
    // keep track of which components have finished
    second_quiz_third_questionComponents = [];
    second_quiz_third_questionComponents.push(resp_quiz_2_q_3);
    
    for (const thisComponent of second_quiz_third_questionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function second_quiz_third_questionRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'second_quiz_third_question'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = second_quiz_third_questionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *resp_quiz_2_q_3* updates
    if (t >= 0.0 && resp_quiz_2_q_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp_quiz_2_q_3.tStart = t;  // (not accounting for frame time here)
      resp_quiz_2_q_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp_quiz_2_q_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp_quiz_2_q_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp_quiz_2_q_3.clearEvents(); });
    }

    if (resp_quiz_2_q_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp_quiz_2_q_3.getKeys({keyList: ['1', '2', '3'], waitRelease: false});
      _resp_quiz_2_q_3_allKeys = _resp_quiz_2_q_3_allKeys.concat(theseKeys);
      if (_resp_quiz_2_q_3_allKeys.length > 0) {
        resp_quiz_2_q_3.keys = _resp_quiz_2_q_3_allKeys[_resp_quiz_2_q_3_allKeys.length - 1].name;  // just the last key pressed
        resp_quiz_2_q_3.rt = _resp_quiz_2_q_3_allKeys[_resp_quiz_2_q_3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of second_quiz_third_questionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var second_stim_quiz_third_question_resultt;
function second_quiz_third_questionRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'second_quiz_third_question'-------
    for (const thisComponent of second_quiz_third_questionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    if (((resp_quiz_2_q_3.keys === "1") && (condition === 1))) {
        quiz_and_attention_check_fails = (quiz_and_attention_check_fails + 1);
        second_stim_quiz_third_question_resultt = "incorrect";
    } else {
        if (((resp_quiz_2_q_3.keys === "2") && (condition === 1))) {
            quiz_and_attention_check_fails = quiz_and_attention_check_fails;
            second_stim_quiz_third_question_result = "correct";
        } else {
            if (((resp_quiz_2_q_3.keys === "3") && (condition === 1))) {
                quiz_and_attention_check_fails = (quiz_and_attention_check_fails + 1);
                second_stim_quiz_third_question_result = "incorrect";
            } else {
                if (((resp_quiz_2_q_3.keys === "1") && (condition === 2))) {
                    quiz_and_attention_check_fails = quiz_and_attention_check_fails;
                    second_stim_quiz_third_question_result = "correct";
                } else {
                    if (((resp_quiz_2_q_3.keys === "2") && (condition === 2))) {
                        quiz_and_attention_check_fails = (quiz_and_attention_check_fails + 1);
                        second_stim_quiz_third_question_result = "incorrect";
                    } else {
                        if (((resp_quiz_2_q_3.keys === "3") && (condition === 2))) {
                            quiz_and_attention_check_fails = (quiz_and_attention_check_fails + 1);
                            second_stim_quiz_third_question_result = "incorrect";
                        }
                    }
                }
            }
        }
    }
    horizontal_feedback_stim.pos = [0, 0.12];
    horizontal_feedback_stim.size = [0.1, 0.1];
    instructions_slide_six.setAutoDraw(false);
    horizontal_feedback_stim.setAutoDraw(false);
    
    psychoJS.experiment.addData('resp_quiz_2_q_3.keys', resp_quiz_2_q_3.keys);
    if (typeof resp_quiz_2_q_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp_quiz_2_q_3.rt', resp_quiz_2_q_3.rt);
        routineTimer.reset();
        }
    
    resp_quiz_2_q_3.stop();
    // the Routine "second_quiz_third_question" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _advance_from_second_quiz_allKeys;
var second_quiz_third_question_reminderComponents;
function second_quiz_third_question_reminderRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'second_quiz_third_question_reminder'-------
    t = 0;
    second_quiz_third_question_reminderClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    if (((second_stim_quiz_third_question_result === "correct") && (condition === 1))) {
        horizontal_feedback_stim.pos = [0, 0.12];
        horizontal_feedback_stim.size = [0.1, 0.1];
        correct_result_plus_zero.setAutoDraw(true);
        horizontal_feedback_stim.setAutoDraw(true);
    } else {
        if (((second_stim_quiz_third_question_result === "incorrect") && (condition === 1))) {
            horizontal_feedback_stim.pos = [0, 0.12];
            horizontal_feedback_stim.size = [0.1, 0.1];
            incorrect_result_plus_zero.setAutoDraw(true);
            horizontal_feedback_stim.setAutoDraw(true);
        } else {
            if (((second_stim_quiz_third_question_result === "correct") && (condition === 2))) {
                horizontal_feedback_stim.pos = [0, 0.12];
                horizontal_feedback_stim.size = [0.1, 0.1];
                correct_result_plus_one.setAutoDraw(true);
                horizontal_feedback_stim.setAutoDraw(true);
            } else {
                if (((second_stim_quiz_third_question_result === "incorrect") && (condition === 2))) {
                    horizontal_feedback_stim.pos = [0, 0.12];
                    horizontal_feedback_stim.size = [0.1, 0.1];
                    incorrect_result_plus_one.setAutoDraw(true);
                    horizontal_feedback_stim.setAutoDraw(true);
                }
            }
        }
    }
    
    advance_from_second_quiz.keys = undefined;
    advance_from_second_quiz.rt = undefined;
    _advance_from_second_quiz_allKeys = [];
    // keep track of which components have finished
    second_quiz_third_question_reminderComponents = [];
    second_quiz_third_question_reminderComponents.push(advance_from_second_quiz);
    
    for (const thisComponent of second_quiz_third_question_reminderComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function second_quiz_third_question_reminderRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'second_quiz_third_question_reminder'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = second_quiz_third_question_reminderClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *advance_from_second_quiz* updates
    if (t >= 0.0 && advance_from_second_quiz.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      advance_from_second_quiz.tStart = t;  // (not accounting for frame time here)
      advance_from_second_quiz.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { advance_from_second_quiz.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { advance_from_second_quiz.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { advance_from_second_quiz.clearEvents(); });
    }

    if (advance_from_second_quiz.status === PsychoJS.Status.STARTED) {
      let theseKeys = advance_from_second_quiz.getKeys({keyList: [], waitRelease: false});
      _advance_from_second_quiz_allKeys = _advance_from_second_quiz_allKeys.concat(theseKeys);
      if (_advance_from_second_quiz_allKeys.length > 0) {
        advance_from_second_quiz.keys = _advance_from_second_quiz_allKeys[_advance_from_second_quiz_allKeys.length - 1].name;  // just the last key pressed
        advance_from_second_quiz.rt = _advance_from_second_quiz_allKeys[_advance_from_second_quiz_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of second_quiz_third_question_reminderComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function second_quiz_third_question_reminderRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'second_quiz_third_question_reminder'-------
    for (const thisComponent of second_quiz_third_question_reminderComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    if (((second_stim_quiz_third_question_result === "correct") && (condition === 1))) {
        horizontal_feedback_stim.pos = [0, 0.12];
        horizontal_feedback_stim.size = [0.1, 0.1];
        correct_result_plus_zero.setAutoDraw(false);
        horizontal_feedback_stim.setAutoDraw(false);
    } else {
        if (((second_stim_quiz_third_question_result === "incorrect") && (condition === 1))) {
            horizontal_feedback_stim.pos = [0, 0.12];
            horizontal_feedback_stim.size = [0.1, 0.1];
            incorrect_result_plus_zero.setAutoDraw(false);
            horizontal_feedback_stim.setAutoDraw(false);
        } else {
            if (((second_stim_quiz_third_question_result === "correct") && (condition === 2))) {
                horizontal_feedback_stim.pos = [0, 0.12];
                horizontal_feedback_stim.size = [0.1, 0.1];
                correct_result_plus_one.setAutoDraw(false);
                horizontal_feedback_stim.setAutoDraw(false);
            } else {
                if (((second_stim_quiz_third_question_result === "incorrect") && (condition === 2))) {
                    horizontal_feedback_stim.pos = [0, 0.12];
                    horizontal_feedback_stim.size = [0.1, 0.1];
                    incorrect_result_plus_one.setAutoDraw(false);
                    horizontal_feedback_stim.setAutoDraw(false);
                }
            }
        }
    }
    
    psychoJS.experiment.addData('advance_from_second_quiz.keys', advance_from_second_quiz.keys);
    if (typeof advance_from_second_quiz.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('advance_from_second_quiz.rt', advance_from_second_quiz.rt);
        routineTimer.reset();
        }
    
    advance_from_second_quiz.stop();
    // the Routine "second_quiz_third_question_reminder" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _advance_from_last_reminder_allKeys;
var last_stim_reminderComponents;
function last_stim_reminderRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'last_stim_reminder'-------
    t = 0;
    last_stim_reminderClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    advance_from_last_reminder.keys = undefined;
    advance_from_last_reminder.rt = undefined;
    _advance_from_last_reminder_allKeys = [];
    if ((condition === 1)) {
        horizontal_feedback_stim.pos = [0, 0.17];
        vertical_feedback_stim.pos = [(- 0.17), 0.17];
        grey_no_feedback_stim.pos = [0.17, 0.17];
        horizontal_feedback_stim.size = [0.1, 0.1];
        vertical_feedback_stim.size = [0.1, 0.1];
        grey_no_feedback_stim.size = [0.1, 0.1];
        result_final_reminder.setAutoDraw(true);
        horizontal_feedback_stim.setAutoDraw(true);
        vertical_feedback_stim.setAutoDraw(true);
        grey_no_feedback_stim.setAutoDraw(true);
    } else {
        if ((condition === 2)) {
            horizontal_feedback_stim.pos = [(- 0.17), 0.17];
            vertical_feedback_stim.pos = [0, 0.17];
            grey_no_feedback_stim.pos = [0.17, 0.17];
            horizontal_feedback_stim.size = [0.1, 0.1];
            vertical_feedback_stim.size = [0.1, 0.1];
            grey_no_feedback_stim.size = [0.1, 0.1];
            result_final_reminder.setAutoDraw(true);
            horizontal_feedback_stim.setAutoDraw(true);
            vertical_feedback_stim.setAutoDraw(true);
            grey_no_feedback_stim.setAutoDraw(true);
        }
    }
    
    // keep track of which components have finished
    last_stim_reminderComponents = [];
    last_stim_reminderComponents.push(advance_from_last_reminder);
    
    for (const thisComponent of last_stim_reminderComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function last_stim_reminderRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'last_stim_reminder'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = last_stim_reminderClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *advance_from_last_reminder* updates
    if (t >= 0.0 && advance_from_last_reminder.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      advance_from_last_reminder.tStart = t;  // (not accounting for frame time here)
      advance_from_last_reminder.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { advance_from_last_reminder.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { advance_from_last_reminder.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { advance_from_last_reminder.clearEvents(); });
    }

    if (advance_from_last_reminder.status === PsychoJS.Status.STARTED) {
      let theseKeys = advance_from_last_reminder.getKeys({keyList: [], waitRelease: false});
      _advance_from_last_reminder_allKeys = _advance_from_last_reminder_allKeys.concat(theseKeys);
      if (_advance_from_last_reminder_allKeys.length > 0) {
        advance_from_last_reminder.keys = _advance_from_last_reminder_allKeys[_advance_from_last_reminder_allKeys.length - 1].name;  // just the last key pressed
        advance_from_last_reminder.rt = _advance_from_last_reminder_allKeys[_advance_from_last_reminder_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of last_stim_reminderComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function last_stim_reminderRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'last_stim_reminder'-------
    for (const thisComponent of last_stim_reminderComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('advance_from_last_reminder.keys', advance_from_last_reminder.keys);
    if (typeof advance_from_last_reminder.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('advance_from_last_reminder.rt', advance_from_last_reminder.rt);
        routineTimer.reset();
        }
    
    advance_from_last_reminder.stop();
    if ((condition === 1)) {
        horizontal_feedback_stim.pos = [0, 0.17];
        vertical_feedback_stim.pos = [(- 0.17), 0.17];
        grey_no_feedback_stim.pos = [0.17, 0.17];
        horizontal_feedback_stim.size = [0.1, 0.1];
        vertical_feedback_stim.size = [0.1, 0.1];
        grey_no_feedback_stim.size = [0.1, 0.1];
        result_final_reminder.setAutoDraw(false);
        horizontal_feedback_stim.setAutoDraw(false);
        vertical_feedback_stim.setAutoDraw(false);
        grey_no_feedback_stim.setAutoDraw(false);
    } else {
        if ((condition === 2)) {
            horizontal_feedback_stim.pos = [(- 0.17), 0.17];
            vertical_feedback_stim.pos = [0, 0.17];
            grey_no_feedback_stim.pos = [0.17, 0.17];
            horizontal_feedback_stim.size = [0.1, 0.1];
            vertical_feedback_stim.size = [0.1, 0.1];
            grey_no_feedback_stim.size = [0.1, 0.1];
            result_final_reminder.setAutoDraw(false);
            horizontal_feedback_stim.setAutoDraw(false);
            vertical_feedback_stim.setAutoDraw(false);
            grey_no_feedback_stim.setAutoDraw(false);
        }
    }
    psychoJS.experiment.addData("second_stim_quiz_first_question_result", second_stim_quiz_first_question_result);
    psychoJS.experiment.addData("second_stim_quiz_second_question_result", second_stim_quiz_second_question_result);
    psychoJS.experiment.addData("second_stim_quiz_third_question_result", second_stim_quiz_third_question_result);
    
    // the Routine "last_stim_reminder" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _enter_main_game_allKeys;
var advance_to_main_taskComponents;
function advance_to_main_taskRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'advance_to_main_task'-------
    t = 0;
    advance_to_main_taskClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    instructions_slide_fourteen.setAutoDraw(true);
    
    enter_main_game.keys = undefined;
    enter_main_game.rt = undefined;
    _enter_main_game_allKeys = [];
    // keep track of which components have finished
    advance_to_main_taskComponents = [];
    advance_to_main_taskComponents.push(enter_main_game);
    
    for (const thisComponent of advance_to_main_taskComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function advance_to_main_taskRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'advance_to_main_task'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = advance_to_main_taskClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *enter_main_game* updates
    if (t >= 0.0 && enter_main_game.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enter_main_game.tStart = t;  // (not accounting for frame time here)
      enter_main_game.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { enter_main_game.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { enter_main_game.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { enter_main_game.clearEvents(); });
    }

    if (enter_main_game.status === PsychoJS.Status.STARTED) {
      let theseKeys = enter_main_game.getKeys({keyList: ['return'], waitRelease: false});
      _enter_main_game_allKeys = _enter_main_game_allKeys.concat(theseKeys);
      if (_enter_main_game_allKeys.length > 0) {
        enter_main_game.keys = _enter_main_game_allKeys[_enter_main_game_allKeys.length - 1].name;  // just the last key pressed
        enter_main_game.rt = _enter_main_game_allKeys[_enter_main_game_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of advance_to_main_taskComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function advance_to_main_taskRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'advance_to_main_task'-------
    for (const thisComponent of advance_to_main_taskComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    instructions_slide_fourteen.setAutoDraw(false);
    
    psychoJS.experiment.addData('enter_main_game.keys', enter_main_game.keys);
    if (typeof enter_main_game.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('enter_main_game.rt', enter_main_game.rt);
        routineTimer.reset();
        }
    
    enter_main_game.stop();
    // the Routine "advance_to_main_task" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_main_allKeys;
var main_taskComponents;
function main_taskRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'main_task'-------
    t = 0;
    main_taskClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    work_total_presses = 0;
    main_trial_num = (main_trial_num + 1);
    psychoJS.experiment.addData("mode", "main");
    psychoJS.experiment.addData("main_trial_num", main_trial_num);
    psychoJS.experiment.addData("calibration_total_presses", calibration_total_presses);
    psychoJS.experiment.addData("maximum_work_for_feedback_threshold", maximum_work_for_feedback_threshold);
    psychoJS.experiment.addData("final_work_for_feedback_threshold", final_work_for_feedback_threshold);
    
    fractal_one_main.setPos([fractal_60_x_pos, fractal_60_y_pos]);
    fractal_one_main.setImage(fractal_60_stim);
    fractal_two_main.setPos([fractal_80_x_pos, fractal_80_y_pos]);
    fractal_two_main.setImage(fractal_80_stim);
    key_resp_main.keys = undefined;
    key_resp_main.rt = undefined;
    _key_resp_main_allKeys = [];
    decision_to_work_for_feedback = [];
    time_of_press_list = [];
    current_work_rate_list = [];
    current_opacity_level_list = [];
    final_opacity_level = [];
    
    // keep track of which components have finished
    main_taskComponents = [];
    main_taskComponents.push(iti_main);
    main_taskComponents.push(fractal_one_main);
    main_taskComponents.push(fractal_two_main);
    main_taskComponents.push(key_resp_main);
    
    for (const thisComponent of main_taskComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function main_taskRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'main_task'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = main_taskClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *iti_main* updates
    if (t >= 0.0 && iti_main.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      iti_main.tStart = t;  // (not accounting for frame time here)
      iti_main.frameNStart = frameN;  // exact frame index
      
      iti_main.setAutoDraw(true);
    }

    frameRemains = 0.0 + iti - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (iti_main.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      iti_main.setAutoDraw(false);
    }
    
    // *fractal_one_main* updates
    if (((iti_main.status == FINISHED)) && fractal_one_main.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fractal_one_main.tStart = t;  // (not accounting for frame time here)
      fractal_one_main.frameNStart = frameN;  // exact frame index
      
      fractal_one_main.setAutoDraw(true);
    }

    if (fractal_one_main.status === PsychoJS.Status.STARTED && t >= (fractal_one_main.tStart + 2.0)) {
      fractal_one_main.setAutoDraw(false);
    }
    
    // *fractal_two_main* updates
    if (((iti_main.status == FINISHED)) && fractal_two_main.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fractal_two_main.tStart = t;  // (not accounting for frame time here)
      fractal_two_main.frameNStart = frameN;  // exact frame index
      
      fractal_two_main.setAutoDraw(true);
    }

    if (fractal_two_main.status === PsychoJS.Status.STARTED && t >= (fractal_two_main.tStart + 2.0)) {
      fractal_two_main.setAutoDraw(false);
    }
    
    // *key_resp_main* updates
    if (((iti_main.status == FINISHED)) && key_resp_main.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_main.tStart = t;  // (not accounting for frame time here)
      key_resp_main.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_main.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_main.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_main.clearEvents(); });
    }

    if (key_resp_main.status === PsychoJS.Status.STARTED && t >= (key_resp_main.tStart + 2.0)) {
      key_resp_main.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp_main.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_main.getKeys({keyList: ['f', 'j'], waitRelease: false});
      _key_resp_main_allKeys = _key_resp_main_allKeys.concat(theseKeys);
      if (_key_resp_main_allKeys.length > 0) {
        key_resp_main.keys = _key_resp_main_allKeys[_key_resp_main_allKeys.length - 1].name;  // just the last key pressed
        key_resp_main.rt = _key_resp_main_allKeys[_key_resp_main_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of main_taskComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function main_taskRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'main_task'-------
    for (const thisComponent of main_taskComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp_main.keys', key_resp_main.keys);
    if (typeof key_resp_main.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_main.rt', key_resp_main.rt);
        routineTimer.reset();
        }
    
    key_resp_main.stop();
    outcome = [];
    side_chosen = [];
    fractal_chosen = [];
    reward = [];
    if ((condition === 1)) {
        if ((((key_resp_main.keys === "f") && (fractal_60_side === "left")) && (fractal_60_reward === 1))) {
            outcome = "good";
            side_chosen = "left";
            fractal_chosen = "fractal_60";
            reward = 1;
            main_total_points = (main_total_points + 1);
        } else {
            if ((((key_resp_main.keys === "f") && (fractal_60_side === "left")) && (fractal_60_reward === 0))) {
                outcome = "bad";
                side_chosen = "left";
                fractal_chosen = "fractal_60";
                reward = 0;
                main_total_points = main_total_points;
            } else {
                if ((((key_resp_main.keys === "j") && (fractal_60_side === "right")) && (fractal_60_reward === 1))) {
                    outcome = "good";
                    side_chosen = "right";
                    fractal_chosen = "fractal_60";
                    reward = 1;
                    main_total_points = (main_total_points + 1);
                } else {
                    if ((((key_resp_main.keys === "j") && (fractal_60_side === "right")) && (fractal_60_reward === 0))) {
                        outcome = "bad";
                        side_chosen = "right";
                        fractal_chosen = "fractal_60";
                        reward = 0;
                        main_total_points = main_total_points;
                    } else {
                        if ((((key_resp_main.keys === "f") && (fractal_80_side === "left")) && (fractal_80_reward === 1))) {
                            outcome = "good";
                            side_chosen = "left";
                            fractal_chosen = "fractal_80";
                            reward = 1;
                            main_total_points = (main_total_points + 1);
                        } else {
                            if ((((key_resp_main.keys === "f") && (fractal_80_side === "left")) && (fractal_80_reward === 0))) {
                                outcome = "bad";
                                side_chosen = "left";
                                fractal_chosen = "fractal_80";
                                reward = 0;
                                main_total_points = main_total_points;
                            } else {
                                if ((((key_resp_main.keys === "j") && (fractal_80_side === "right")) && (fractal_80_reward === 1))) {
                                    outcome = "good";
                                    side_chosen = "right";
                                    fractal_chosen = "fractal_80";
                                    reward = 1;
                                    main_total_points = (main_total_points + 1);
                                } else {
                                    if ((((key_resp_main.keys === "j") && (fractal_80_side === "right")) && (fractal_80_reward === 0))) {
                                        outcome = "bad";
                                        side_chosen = "right";
                                        fractal_chosen = "fractal_80";
                                        reward = 0;
                                        main_total_points = main_total_points;
                                    } else {
                                        outcome = "missed";
                                        side_chosen = "n/a";
                                        fractal_chosen = "n/a";
                                        reward = 0;
                                        main_total_points = main_total_points;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    } else {
        if ((condition === 2)) {
            if ((((key_resp_main.keys === "f") && (fractal_60_side === "left")) && (fractal_60_reward === 1))) {
                outcome = "good";
                side_chosen = "left";
                fractal_chosen = "fractal_60";
                reward = 1;
                main_total_points = (main_total_points + 1);
            } else {
                if ((((key_resp_main.keys === "f") && (fractal_60_side === "left")) && (fractal_60_reward === 0))) {
                    outcome = "bad";
                    side_chosen = "left";
                    fractal_chosen = "fractal_60";
                    reward = 0;
                    main_total_points = main_total_points;
                } else {
                    if ((((key_resp_main.keys === "j") && (fractal_60_side === "right")) && (fractal_60_reward === 1))) {
                        outcome = "good";
                        side_chosen = "right";
                        fractal_chosen = "fractal_60";
                        reward = 1;
                        main_total_points = (main_total_points + 1);
                    } else {
                        if ((((key_resp_main.keys === "j") && (fractal_60_side === "right")) && (fractal_60_reward === 0))) {
                            outcome = "bad";
                            side_chosen = "right";
                            fractal_chosen = "fractal_60";
                            reward = 0;
                            main_total_points = main_total_points;
                        } else {
                            if ((((key_resp_main.keys === "f") && (fractal_80_side === "left")) && (fractal_80_reward === 1))) {
                                outcome = "good";
                                side_chosen = "left";
                                fractal_chosen = "fractal_80";
                                reward = 1;
                                main_total_points = (main_total_points + 1);
                            } else {
                                if ((((key_resp_main.keys === "f") && (fractal_80_side === "left")) && (fractal_80_reward === 0))) {
                                    outcome = "bad";
                                    side_chosen = "left";
                                    fractal_chosen = "fractal_80";
                                    reward = 0;
                                    main_total_points = main_total_points;
                                } else {
                                    if ((((key_resp_main.keys === "j") && (fractal_80_side === "right")) && (fractal_80_reward === 1))) {
                                        outcome = "good";
                                        side_chosen = "right";
                                        fractal_chosen = "fractal_80";
                                        reward = 1;
                                        main_total_points = (main_total_points + 1);
                                    } else {
                                        if ((((key_resp_main.keys === "j") && (fractal_80_side === "right")) && (fractal_80_reward === 0))) {
                                            outcome = "bad";
                                            side_chosen = "right";
                                            fractal_chosen = "fractal_80";
                                            reward = 0;
                                            main_total_points = main_total_points;
                                        } else {
                                            outcome = "missed";
                                            side_chosen = "n/a";
                                            fractal_chosen = "n/a";
                                            reward = 0;
                                            main_total_points = main_total_points;
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    psychoJS.experiment.addData("side_chosen", side_chosen);
    psychoJS.experiment.addData("fractal_chosen", fractal_chosen);
    psychoJS.experiment.addData("reward", reward);
    psychoJS.experiment.addData("total_points", main_total_points);
    
    load_feedback_stim_to_draw = [];
    if ((((feedback_outcome === "veridical_feedback") && (outcome === "good")) && (condition === 1))) {
        decision_to_work_for_feedback = "n/a";
        load_feedback_stim_to_draw = vertical_feedback_stim;
    } else {
        if ((((feedback_outcome === "veridical_feedback") && (outcome === "bad")) && (condition === 1))) {
            decision_to_work_for_feedback = "n/a";
            load_feedback_stim_to_draw = horizontal_feedback_stim;
        } else {
            if ((((feedback_outcome === "veridical_feedback") && (outcome === "good")) && (condition === 2))) {
                decision_to_work_for_feedback = "n/a";
                load_feedback_stim_to_draw = horizontal_feedback_stim;
            } else {
                if ((((feedback_outcome === "veridical_feedback") && (outcome === "bad")) && (condition === 2))) {
                    decision_to_work_for_feedback = "n/a";
                    load_feedback_stim_to_draw = vertical_feedback_stim;
                } else {
                    if ((outcome === "missed")) {
                        decision_to_work_for_feedback = "missed_trial";
                    } else {
                        if ((feedback_outcome === "no_feedback")) {
                            decision_to_work_for_feedback = "n/a";
                            load_feedback_stim_to_draw = grey_no_feedback_stim;
                        } else {
                            if ((feedback_outcome === "work_option")) {
                                decision_to_work_for_feedback = "probe";
                                load_feedback_stim_to_draw = grey_no_feedback_stim;
                            }
                        }
                    }
                }
            }
        }
    }
    do_not_do_feedback = [];
    do_feedback = [];
    if ((decision_to_work_for_feedback === "n/a")) {
        do_not_do_feedback = 1;
        do_feedback = 0;
        draw_miss = 0;
    } else {
        if ((decision_to_work_for_feedback === "probe")) {
            do_not_do_feedback = 0;
            do_feedback = 1;
            draw_miss = 0;
        } else {
            if ((decision_to_work_for_feedback === "missed_trial")) {
                do_not_do_feedback = 0;
                do_feedback = 0;
                draw_miss = 1;
            }
        }
    }
    
    // the Routine "main_task" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var completed_main_taskComponents;
function completed_main_taskRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'completed_main_task'-------
    t = 0;
    completed_main_taskClock.reset(); // clock
    frameN = -1;
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    completed_main_taskComponents = [];
    completed_main_taskComponents.push(post_task_image);
    
    for (const thisComponent of completed_main_taskComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function completed_main_taskRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'completed_main_task'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = completed_main_taskClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *post_task_image* updates
    if (t >= 0.0 && post_task_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      post_task_image.tStart = t;  // (not accounting for frame time here)
      post_task_image.frameNStart = frameN;  // exact frame index
      
      post_task_image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (post_task_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      post_task_image.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of completed_main_taskComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function completed_main_taskRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'completed_main_task'-------
    for (const thisComponent of completed_main_taskComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _go_to_fractal_question_allKeys;
var continue_to_fractal_questionComponents;
function continue_to_fractal_questionRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'continue_to_fractal_question'-------
    t = 0;
    continue_to_fractal_questionClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    post_task_continue_slide.setAutoDraw(true);
    
    go_to_fractal_question.keys = undefined;
    go_to_fractal_question.rt = undefined;
    _go_to_fractal_question_allKeys = [];
    // keep track of which components have finished
    continue_to_fractal_questionComponents = [];
    continue_to_fractal_questionComponents.push(go_to_fractal_question);
    
    for (const thisComponent of continue_to_fractal_questionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function continue_to_fractal_questionRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'continue_to_fractal_question'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = continue_to_fractal_questionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *go_to_fractal_question* updates
    if (t >= 0.0 && go_to_fractal_question.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      go_to_fractal_question.tStart = t;  // (not accounting for frame time here)
      go_to_fractal_question.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { go_to_fractal_question.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { go_to_fractal_question.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { go_to_fractal_question.clearEvents(); });
    }

    if (go_to_fractal_question.status === PsychoJS.Status.STARTED) {
      let theseKeys = go_to_fractal_question.getKeys({keyList: [], waitRelease: false});
      _go_to_fractal_question_allKeys = _go_to_fractal_question_allKeys.concat(theseKeys);
      if (_go_to_fractal_question_allKeys.length > 0) {
        go_to_fractal_question.keys = _go_to_fractal_question_allKeys[_go_to_fractal_question_allKeys.length - 1].name;  // just the last key pressed
        go_to_fractal_question.rt = _go_to_fractal_question_allKeys[_go_to_fractal_question_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of continue_to_fractal_questionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function continue_to_fractal_questionRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'continue_to_fractal_question'-------
    for (const thisComponent of continue_to_fractal_questionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    post_task_continue_slide.setAutoDraw(false);
    
    psychoJS.experiment.addData('go_to_fractal_question.keys', go_to_fractal_question.keys);
    if (typeof go_to_fractal_question.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('go_to_fractal_question.rt', go_to_fractal_question.rt);
        routineTimer.reset();
        }
    
    go_to_fractal_question.stop();
    // the Routine "continue_to_fractal_question" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var better_fractal;
var _choose_fractal_allKeys;
var post_task_fractal_questionComponents;
function post_task_fractal_questionRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'post_task_fractal_question'-------
    t = 0;
    post_task_fractal_questionClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    better_fractal = [];
    if ((post_task_fractal_selection === 1)) {
        fractal_blossom.pos = [(- 0.2), 0.04];
        fractal_octopus.pos = [0.2, 0.04];
        post_task_fractal_slide.setAutoDraw(true);
        fractal_blossom.setAutoDraw(true);
        fractal_octopus.setAutoDraw(true);
    } else {
        if ((post_task_fractal_selection === 2)) {
            fractal_blossom.pos = [0.2, 0.04];
            fractal_octopus.pos = [(- 0.2), 0.04];
            post_task_fractal_slide.setAutoDraw(true);
            fractal_blossom.setAutoDraw(true);
            fractal_octopus.setAutoDraw(true);
        }
    }
    
    choose_fractal.keys = undefined;
    choose_fractal.rt = undefined;
    _choose_fractal_allKeys = [];
    // keep track of which components have finished
    post_task_fractal_questionComponents = [];
    post_task_fractal_questionComponents.push(choose_fractal);
    
    for (const thisComponent of post_task_fractal_questionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function post_task_fractal_questionRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'post_task_fractal_question'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = post_task_fractal_questionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *choose_fractal* updates
    if (t >= 0.0 && choose_fractal.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choose_fractal.tStart = t;  // (not accounting for frame time here)
      choose_fractal.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { choose_fractal.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { choose_fractal.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { choose_fractal.clearEvents(); });
    }

    if (choose_fractal.status === PsychoJS.Status.STARTED) {
      let theseKeys = choose_fractal.getKeys({keyList: ['1', '2'], waitRelease: false});
      _choose_fractal_allKeys = _choose_fractal_allKeys.concat(theseKeys);
      if (_choose_fractal_allKeys.length > 0) {
        choose_fractal.keys = _choose_fractal_allKeys[_choose_fractal_allKeys.length - 1].name;  // just the last key pressed
        choose_fractal.rt = _choose_fractal_allKeys[_choose_fractal_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of post_task_fractal_questionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function post_task_fractal_questionRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'post_task_fractal_question'-------
    for (const thisComponent of post_task_fractal_questionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    better_fractal = [];
    if ((post_task_fractal_selection === 1)) {
        fractal_blossom.pos = [0.2, 0.04];
        fractal_octopus.pos = [(- 0.2), 0.04];
        post_task_fractal_slide.setAutoDraw(false);
        fractal_blossom.setAutoDraw(false);
        fractal_octopus.setAutoDraw(false);
    } else {
        if ((post_task_fractal_selection === 2)) {
            fractal_blossom.pos = [(- 0.2), 0.04];
            fractal_octopus.pos = [0.2, 0.04];
            post_task_fractal_slide.setAutoDraw(false);
            fractal_blossom.setAutoDraw(false);
            fractal_octopus.setAutoDraw(false);
        }
    }
    if (((post_task_fractal_selection === 1) && (choose_fractal.keys === "1"))) {
        better_fractal = "blossom";
    } else {
        if (((post_task_fractal_selection === 1) && (choose_fractal.keys === "2"))) {
            better_fractal = "octopus";
        } else {
            if (((post_task_fractal_selection === 2) && (choose_fractal.keys === "1"))) {
                better_fractal = "octopus";
            } else {
                if (((post_task_fractal_selection === 2) && (choose_fractal.keys === "2"))) {
                    better_fractal = "blossom";
                }
            }
        }
    }
    psychoJS.experiment.addData("better_fractal", better_fractal);
    
    psychoJS.experiment.addData('choose_fractal.keys', choose_fractal.keys);
    if (typeof choose_fractal.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('choose_fractal.rt', choose_fractal.rt);
        routineTimer.reset();
        }
    
    choose_fractal.stop();
    // the Routine "post_task_fractal_question" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var SAM_hu_question_2Components;
function SAM_hu_question_2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'SAM_hu_question_2'-------
    t = 0;
    SAM_hu_question_2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // setup some python lists for storing info about the select_answer_mouse_3
    select_answer_mouse_3.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    SAM_hu_question_2Components = [];
    SAM_hu_question_2Components.push(SAM_hu_2);
    SAM_hu_question_2Components.push(choice_1_post);
    SAM_hu_question_2Components.push(choice_2_post);
    SAM_hu_question_2Components.push(choice_3_post);
    SAM_hu_question_2Components.push(choice_4_post);
    SAM_hu_question_2Components.push(choice_5_post);
    SAM_hu_question_2Components.push(choice_6_post);
    SAM_hu_question_2Components.push(choice_7_post);
    SAM_hu_question_2Components.push(choice_8_post);
    SAM_hu_question_2Components.push(choice_9_post);
    SAM_hu_question_2Components.push(select_answer_mouse_3);
    
    for (const thisComponent of SAM_hu_question_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function SAM_hu_question_2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'SAM_hu_question_2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = SAM_hu_question_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *SAM_hu_2* updates
    if (t >= 0.0 && SAM_hu_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SAM_hu_2.tStart = t;  // (not accounting for frame time here)
      SAM_hu_2.frameNStart = frameN;  // exact frame index
      
      SAM_hu_2.setAutoDraw(true);
    }

    
    // *choice_1_post* updates
    if (t >= 0.0 && choice_1_post.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_1_post.tStart = t;  // (not accounting for frame time here)
      choice_1_post.frameNStart = frameN;  // exact frame index
      
      choice_1_post.setAutoDraw(true);
    }

    
    // *choice_2_post* updates
    if (t >= 0.0 && choice_2_post.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_2_post.tStart = t;  // (not accounting for frame time here)
      choice_2_post.frameNStart = frameN;  // exact frame index
      
      choice_2_post.setAutoDraw(true);
    }

    
    // *choice_3_post* updates
    if (t >= 0.0 && choice_3_post.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_3_post.tStart = t;  // (not accounting for frame time here)
      choice_3_post.frameNStart = frameN;  // exact frame index
      
      choice_3_post.setAutoDraw(true);
    }

    
    // *choice_4_post* updates
    if (t >= 0.0 && choice_4_post.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_4_post.tStart = t;  // (not accounting for frame time here)
      choice_4_post.frameNStart = frameN;  // exact frame index
      
      choice_4_post.setAutoDraw(true);
    }

    
    // *choice_5_post* updates
    if (t >= 0.0 && choice_5_post.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_5_post.tStart = t;  // (not accounting for frame time here)
      choice_5_post.frameNStart = frameN;  // exact frame index
      
      choice_5_post.setAutoDraw(true);
    }

    
    // *choice_6_post* updates
    if (t >= 0.0 && choice_6_post.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_6_post.tStart = t;  // (not accounting for frame time here)
      choice_6_post.frameNStart = frameN;  // exact frame index
      
      choice_6_post.setAutoDraw(true);
    }

    
    // *choice_7_post* updates
    if (t >= 0.0 && choice_7_post.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_7_post.tStart = t;  // (not accounting for frame time here)
      choice_7_post.frameNStart = frameN;  // exact frame index
      
      choice_7_post.setAutoDraw(true);
    }

    
    // *choice_8_post* updates
    if (t >= 0.0 && choice_8_post.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_8_post.tStart = t;  // (not accounting for frame time here)
      choice_8_post.frameNStart = frameN;  // exact frame index
      
      choice_8_post.setAutoDraw(true);
    }

    
    // *choice_9_post* updates
    if (t >= 0.0 && choice_9_post.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_9_post.tStart = t;  // (not accounting for frame time here)
      choice_9_post.frameNStart = frameN;  // exact frame index
      
      choice_9_post.setAutoDraw(true);
    }

    // *select_answer_mouse_3* updates
    if (t >= 0.0 && select_answer_mouse_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      select_answer_mouse_3.tStart = t;  // (not accounting for frame time here)
      select_answer_mouse_3.frameNStart = frameN;  // exact frame index
      
      select_answer_mouse_3.status = PsychoJS.Status.STARTED;
      select_answer_mouse_3.mouseClock.reset();
      prevButtonState = select_answer_mouse_3.getPressed();  // if button is down already this ISN'T a new click
      }
    if (select_answer_mouse_3.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = select_answer_mouse_3.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [choice_1_post,choice_2_post,choice_3_post,choice_4_post,choice_5_post,choice_6_post,choice_7_post,choice_8_post,choice_9_post]) {
            if (obj.contains(select_answer_mouse_3)) {
              gotValidClick = true;
              select_answer_mouse_3.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of SAM_hu_question_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SAM_hu_question_2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'SAM_hu_question_2'-------
    for (const thisComponent of SAM_hu_question_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for thisExp (ExperimentHandler)
    _mouseXYs = select_answer_mouse_3.getPos();
    _mouseButtons = select_answer_mouse_3.getPressed();
    psychoJS.experiment.addData('select_answer_mouse_3.x', _mouseXYs[0]);
    psychoJS.experiment.addData('select_answer_mouse_3.y', _mouseXYs[1]);
    psychoJS.experiment.addData('select_answer_mouse_3.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('select_answer_mouse_3.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('select_answer_mouse_3.rightButton', _mouseButtons[2]);
    if (select_answer_mouse_3.clicked_name.length > 0) {
      psychoJS.experiment.addData('select_answer_mouse_3.clicked_name', select_answer_mouse_3.clicked_name[0]);}
    answer_to_draw = [];
    for (var answer, _pj_c = 0, _pj_a = [choice_1_post, choice_2_post, choice_3_post, choice_4_post, choice_5_post, choice_6_post, choice_7_post, choice_8_post, choice_9_post], _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        answer = _pj_a[_pj_c];
        if (select_answer_mouse_3.isPressedIn(answer)) {
            answer_to_draw = answer;
        }
    }
    
    // the Routine "SAM_hu_question_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var highlight_post_sam_huComponents;
function highlight_post_sam_huRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'highlight_post_sam_hu'-------
    t = 0;
    highlight_post_sam_huClock.reset(); // clock
    frameN = -1;
    routineTimer.add(0.300000);
    // update component parameters for each repeat
    // keep track of which components have finished
    highlight_post_sam_huComponents = [];
    highlight_post_sam_huComponents.push(sam_hu_highlight_post);
    
    for (const thisComponent of highlight_post_sam_huComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function highlight_post_sam_huRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'highlight_post_sam_hu'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = highlight_post_sam_huClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *sam_hu_highlight_post* updates
    if (t >= 0.0 && sam_hu_highlight_post.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sam_hu_highlight_post.tStart = t;  // (not accounting for frame time here)
      sam_hu_highlight_post.frameNStart = frameN;  // exact frame index
      
      sam_hu_highlight_post.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (sam_hu_highlight_post.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      sam_hu_highlight_post.setAutoDraw(false);
    }
    answer_to_draw.fillColor = [0.3, 0.5, 0.7];
    answer_to_draw.setAutoDraw(true);
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of highlight_post_sam_huComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function highlight_post_sam_huRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'highlight_post_sam_hu'-------
    for (const thisComponent of highlight_post_sam_huComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    answer_to_draw.setAutoDraw(false);
    
    return Scheduler.Event.NEXT;
  };
}


var SAM_ec_question_2Components;
function SAM_ec_question_2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'SAM_ec_question_2'-------
    t = 0;
    SAM_ec_question_2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // setup some python lists for storing info about the select_answer_mouse_4
    select_answer_mouse_4.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    SAM_ec_question_2Components = [];
    SAM_ec_question_2Components.push(SAM_ec_2);
    SAM_ec_question_2Components.push(choice_num_1_post);
    SAM_ec_question_2Components.push(choice_num_2_post);
    SAM_ec_question_2Components.push(choice_num_3_post);
    SAM_ec_question_2Components.push(choice_num_4_post);
    SAM_ec_question_2Components.push(choice_num_5_post);
    SAM_ec_question_2Components.push(choice_num_6_post);
    SAM_ec_question_2Components.push(choice_num_7_post);
    SAM_ec_question_2Components.push(choice_num_8_post);
    SAM_ec_question_2Components.push(choice_num_9_post);
    SAM_ec_question_2Components.push(select_answer_mouse_4);
    
    for (const thisComponent of SAM_ec_question_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function SAM_ec_question_2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'SAM_ec_question_2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = SAM_ec_question_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *SAM_ec_2* updates
    if (t >= 0.0 && SAM_ec_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SAM_ec_2.tStart = t;  // (not accounting for frame time here)
      SAM_ec_2.frameNStart = frameN;  // exact frame index
      
      SAM_ec_2.setAutoDraw(true);
    }

    
    // *choice_num_1_post* updates
    if (t >= 0.0 && choice_num_1_post.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_num_1_post.tStart = t;  // (not accounting for frame time here)
      choice_num_1_post.frameNStart = frameN;  // exact frame index
      
      choice_num_1_post.setAutoDraw(true);
    }

    
    // *choice_num_2_post* updates
    if (t >= 0.0 && choice_num_2_post.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_num_2_post.tStart = t;  // (not accounting for frame time here)
      choice_num_2_post.frameNStart = frameN;  // exact frame index
      
      choice_num_2_post.setAutoDraw(true);
    }

    
    // *choice_num_3_post* updates
    if (t >= 0.0 && choice_num_3_post.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_num_3_post.tStart = t;  // (not accounting for frame time here)
      choice_num_3_post.frameNStart = frameN;  // exact frame index
      
      choice_num_3_post.setAutoDraw(true);
    }

    
    // *choice_num_4_post* updates
    if (t >= 0.0 && choice_num_4_post.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_num_4_post.tStart = t;  // (not accounting for frame time here)
      choice_num_4_post.frameNStart = frameN;  // exact frame index
      
      choice_num_4_post.setAutoDraw(true);
    }

    
    // *choice_num_5_post* updates
    if (t >= 0.0 && choice_num_5_post.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_num_5_post.tStart = t;  // (not accounting for frame time here)
      choice_num_5_post.frameNStart = frameN;  // exact frame index
      
      choice_num_5_post.setAutoDraw(true);
    }

    
    // *choice_num_6_post* updates
    if (t >= 0.0 && choice_num_6_post.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_num_6_post.tStart = t;  // (not accounting for frame time here)
      choice_num_6_post.frameNStart = frameN;  // exact frame index
      
      choice_num_6_post.setAutoDraw(true);
    }

    
    // *choice_num_7_post* updates
    if (t >= 0.0 && choice_num_7_post.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_num_7_post.tStart = t;  // (not accounting for frame time here)
      choice_num_7_post.frameNStart = frameN;  // exact frame index
      
      choice_num_7_post.setAutoDraw(true);
    }

    
    // *choice_num_8_post* updates
    if (t >= 0.0 && choice_num_8_post.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_num_8_post.tStart = t;  // (not accounting for frame time here)
      choice_num_8_post.frameNStart = frameN;  // exact frame index
      
      choice_num_8_post.setAutoDraw(true);
    }

    
    // *choice_num_9_post* updates
    if (t >= 0.0 && choice_num_9_post.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_num_9_post.tStart = t;  // (not accounting for frame time here)
      choice_num_9_post.frameNStart = frameN;  // exact frame index
      
      choice_num_9_post.setAutoDraw(true);
    }

    // *select_answer_mouse_4* updates
    if (t >= 0.0 && select_answer_mouse_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      select_answer_mouse_4.tStart = t;  // (not accounting for frame time here)
      select_answer_mouse_4.frameNStart = frameN;  // exact frame index
      
      select_answer_mouse_4.status = PsychoJS.Status.STARTED;
      select_answer_mouse_4.mouseClock.reset();
      prevButtonState = select_answer_mouse_4.getPressed();  // if button is down already this ISN'T a new click
      }
    if (select_answer_mouse_4.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = select_answer_mouse_4.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [choice_num_1_post,choice_num_2_post,choice_num_3_post,choice_num_4_post,choice_num_5_post,choice_num_6_post,choice_num_7_post,choice_num_8_post,choice_num_9_post]) {
            if (obj.contains(select_answer_mouse_4)) {
              gotValidClick = true;
              select_answer_mouse_4.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of SAM_ec_question_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SAM_ec_question_2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'SAM_ec_question_2'-------
    for (const thisComponent of SAM_ec_question_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for thisExp (ExperimentHandler)
    _mouseXYs = select_answer_mouse_4.getPos();
    _mouseButtons = select_answer_mouse_4.getPressed();
    psychoJS.experiment.addData('select_answer_mouse_4.x', _mouseXYs[0]);
    psychoJS.experiment.addData('select_answer_mouse_4.y', _mouseXYs[1]);
    psychoJS.experiment.addData('select_answer_mouse_4.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('select_answer_mouse_4.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('select_answer_mouse_4.rightButton', _mouseButtons[2]);
    if (select_answer_mouse_4.clicked_name.length > 0) {
      psychoJS.experiment.addData('select_answer_mouse_4.clicked_name', select_answer_mouse_4.clicked_name[0]);}
    answer_to_draw = [];
    for (var answer, _pj_c = 0, _pj_a = [choice_num_1_post, choice_num_2_post, choice_num_3_post, choice_num_4_post, choice_num_5_post, choice_num_6_post, choice_num_7_post, choice_num_8_post, choice_num_9_post], _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        answer = _pj_a[_pj_c];
        if (select_answer_mouse_4.isPressedIn(answer)) {
            answer_to_draw = answer;
        }
    }
    
    // the Routine "SAM_ec_question_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var highlight_sam_ec_post_choiceComponents;
function highlight_sam_ec_post_choiceRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'highlight_sam_ec_post_choice'-------
    t = 0;
    highlight_sam_ec_post_choiceClock.reset(); // clock
    frameN = -1;
    routineTimer.add(0.300000);
    // update component parameters for each repeat
    // keep track of which components have finished
    highlight_sam_ec_post_choiceComponents = [];
    highlight_sam_ec_post_choiceComponents.push(sam_ec_post_highlight);
    
    for (const thisComponent of highlight_sam_ec_post_choiceComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function highlight_sam_ec_post_choiceRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'highlight_sam_ec_post_choice'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = highlight_sam_ec_post_choiceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *sam_ec_post_highlight* updates
    if (t >= 0.0 && sam_ec_post_highlight.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sam_ec_post_highlight.tStart = t;  // (not accounting for frame time here)
      sam_ec_post_highlight.frameNStart = frameN;  // exact frame index
      
      sam_ec_post_highlight.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (sam_ec_post_highlight.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      sam_ec_post_highlight.setAutoDraw(false);
    }
    answer_to_draw.fillColor = [0.3, 0.5, 0.7];
    answer_to_draw.setAutoDraw(true);
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of highlight_sam_ec_post_choiceComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function highlight_sam_ec_post_choiceRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'highlight_sam_ec_post_choice'-------
    for (const thisComponent of highlight_sam_ec_post_choiceComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    answer_to_draw.setAutoDraw(false);
    
    return Scheduler.Event.NEXT;
  };
}


var _exit_task_allKeys;
var total_points_end_experimentComponents;
function total_points_end_experimentRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'total_points_end_experiment'-------
    t = 0;
    total_points_end_experimentClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    final_total_points.setText(main_total_points);
    exit_task.keys = undefined;
    exit_task.rt = undefined;
    _exit_task_allKeys = [];
    // keep track of which components have finished
    total_points_end_experimentComponents = [];
    total_points_end_experimentComponents.push(final_total_points);
    total_points_end_experimentComponents.push(rest_of_text);
    total_points_end_experimentComponents.push(exit_task);
    
    for (const thisComponent of total_points_end_experimentComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function total_points_end_experimentRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'total_points_end_experiment'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = total_points_end_experimentClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *final_total_points* updates
    if (t >= 0.0 && final_total_points.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      final_total_points.tStart = t;  // (not accounting for frame time here)
      final_total_points.frameNStart = frameN;  // exact frame index
      
      final_total_points.setAutoDraw(true);
    }

    
    // *rest_of_text* updates
    if (t >= 0.0 && rest_of_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rest_of_text.tStart = t;  // (not accounting for frame time here)
      rest_of_text.frameNStart = frameN;  // exact frame index
      
      rest_of_text.setAutoDraw(true);
    }

    
    // *exit_task* updates
    if (t >= 0.0 && exit_task.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      exit_task.tStart = t;  // (not accounting for frame time here)
      exit_task.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { exit_task.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { exit_task.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { exit_task.clearEvents(); });
    }

    if (exit_task.status === PsychoJS.Status.STARTED) {
      let theseKeys = exit_task.getKeys({keyList: [], waitRelease: false});
      _exit_task_allKeys = _exit_task_allKeys.concat(theseKeys);
      if (_exit_task_allKeys.length > 0) {
        exit_task.keys = _exit_task_allKeys[_exit_task_allKeys.length - 1].name;  // just the last key pressed
        exit_task.rt = _exit_task_allKeys[_exit_task_allKeys.length - 1].rt;
        // was this correct?
        if (exit_task.keys == '') {
            exit_task.corr = 1;
        } else {
            exit_task.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of total_points_end_experimentComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function total_points_end_experimentRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'total_points_end_experiment'-------
    for (const thisComponent of total_points_end_experimentComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (exit_task.keys === undefined) {
      if (['None','none',undefined].includes('')) {
         exit_task.corr = 1;  // correct non-response
      } else {
         exit_task.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('exit_task.keys', exit_task.keys);
    psychoJS.experiment.addData('exit_task.corr', exit_task.corr);
    if (typeof exit_task.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('exit_task.rt', exit_task.rt);
        routineTimer.reset();
        }
    
    exit_task.stop();
    // the Routine "total_points_end_experiment" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
