#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_behaviors.binselectie_sm import binSelectieSM
from ariac_flexbe_states.message_state import MessageState
from ariac_support_flexbe_states.equal_state import EqualState
from ariac_flexbe_states.srdf_state_to_moveit_ariac_state import SrdfStateToMoveitAriac
from ariac_flexbe_states.moveit_to_joints_dyn_ariac_state import MoveitToJointsDynAriacState
from ariac_flexbe_states.detect_part_camera_ariac_state import DetectPartCameraAriacState
from flexbe_states.wait_state import WaitState
from ariac_flexbe_states.compute_grasp_ariac_state import ComputeGraspAriacState
from ariac_flexbe_states.vacuum_gripper_control_state import VacuumGripperControlState
from ariac_support_flexbe_states.replace_state import ReplaceState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed Apr 22 2020
@author: Gerard Harkema
'''
class transport_part_form_bin_to_agv_stateSM(Behavior):
	'''
	transports part from it's bin to the selected agv
	'''


	def __init__(self):
		super(transport_part_form_bin_to_agv_stateSM, self).__init__()
		self.name = 'transport_part_form_bin_to_agv_state'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(binSelectieSM, 'binSelectie')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1770 y:298, x:81 y:372
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['part_type', 'agv_id', 'pose_on_agv', 'camera_ref_frame', 'camera_frame'], output_keys=['part_type', 'camera_ref_frame', 'camera_frame'])
		_state_machine.userdata.part_type = ''
		_state_machine.userdata.agv_id = ''
		_state_machine.userdata.move_group_prefix1 = '/ariac/arm1'
		_state_machine.userdata.move_group_prefix2 = '/ariac/arm2'
		_state_machine.userdata.move_group = 'manipulator'
		_state_machine.userdata.tool_link = 'ee_link'
		_state_machine.userdata.part_pose = []
		_state_machine.userdata.joint_values = []
		_state_machine.userdata.action_topic = '/move_group'
		_state_machine.userdata.robot_name = ''
		_state_machine.userdata.pose_on_agv = []
		_state_machine.userdata.config_name_bin1PreGrasp = 'bin1PreGrasp'
		_state_machine.userdata.camera_ref_frame2 = 'arm2_linear_arm_actuator'
		_state_machine.userdata.camera_ref_frame1 = 'arm1_linear_arm_actuator'
		_state_machine.userdata.camera_frame2 = 'logical_camera_2_frame'
		_state_machine.userdata.camera_frame3 = 'logical_camera_3_frame'
		_state_machine.userdata.camera_frame4 = 'logical_camera_4_frame'
		_state_machine.userdata.config_name_bin2PreGrasp = 'bin2PreGrasp'
		_state_machine.userdata.config_name_bin5PreGrasp = 'bin5PreGrasp'
		_state_machine.userdata.camera_ref_frame = ''
		_state_machine.userdata.camera_frame = ''
		_state_machine.userdata.camera_frame1 = 'logical_camera_1_frame'
		_state_machine.userdata.config_name_bin6PreGrasp = 'bin6PreGrasp'
		_state_machine.userdata.joint_names = ''
		_state_machine.userdata.part_rotation = 0
		_state_machine.userdata.arm_id = 'arm1'
		_state_machine.userdata.gripper1 = 'arm1'
		_state_machine.userdata.gripper2 = 'arm2'

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:71 y:54
			OperatableStateMachine.add('binSelectie',
										self.use_behavior(binSelectieSM, 'binSelectie'),
										transitions={'finished': 'arm1', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'part_type': 'part_type', 'camera_topic': 'camera_topic', 'camera_ref_frame': 'camera_ref_frame', 'camera_frame': 'camera_frame', 'part_offset': 'part_offset'})

			# x:1675 y:697
			OperatableStateMachine.add('PartTypeMessage',
										MessageState(),
										transitions={'continue': 'MoseMessage'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'part_type'})

			# x:1675 y:758
			OperatableStateMachine.add('AgvIdMessage',
										MessageState(),
										transitions={'continue': 'PartTypeMessage'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'agv_id'})

			# x:262 y:58
			OperatableStateMachine.add('arm1',
										EqualState(),
										transitions={'true': 'bin5', 'false': 'arm2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'camera_ref_frame', 'value_b': 'camera_ref_frame1'})

			# x:266 y:389
			OperatableStateMachine.add('arm2',
										EqualState(),
										transitions={'true': 'bin1', 'false': 'failed'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'camera_ref_frame', 'value_b': 'camera_ref_frame2'})

			# x:470 y:353
			OperatableStateMachine.add('bin1',
										EqualState(),
										transitions={'true': 'pregraspbin1', 'false': 'bin2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'camera_frame', 'value_b': 'camera_frame3'})

			# x:475 y:527
			OperatableStateMachine.add('bin2',
										EqualState(),
										transitions={'true': 'pregraspbin2', 'false': 'failed'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'camera_frame', 'value_b': 'camera_frame4'})

			# x:467 y:59
			OperatableStateMachine.add('bin5',
										EqualState(),
										transitions={'true': 'pregraspbin5', 'false': 'bin6'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'camera_frame', 'value_b': 'camera_frame1'})

			# x:470 y:277
			OperatableStateMachine.add('bin6',
										EqualState(),
										transitions={'true': 'pregraspbin6', 'false': 'failed'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'camera_frame', 'value_b': 'camera_frame2'})

			# x:663 y:58
			OperatableStateMachine.add('pregraspbin5',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'detectpartbin5', 'planning_failed': 'failed', 'control_failed': 'detectpartbin5', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_bin5PreGrasp', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix1', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:652 y:273
			OperatableStateMachine.add('pregraspbin6',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'detectpartbin6', 'planning_failed': 'failed', 'control_failed': 'detectpartbin6', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_bin6PreGrasp', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix1', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:653 y:351
			OperatableStateMachine.add('pregraspbin1',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'detectpartbin1', 'planning_failed': 'failed', 'control_failed': 'detectpartbin1', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_bin1PreGrasp', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix2', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:657 y:531
			OperatableStateMachine.add('pregraspbin2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'detectpartbin2', 'planning_failed': 'failed', 'control_failed': 'detectpartbin2', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_bin2PreGrasp', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix2', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1164 y:44
			OperatableStateMachine.add('pickbin5',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'gripperkeuze', 'planning_failed': 'failed', 'control_failed': 'Retry'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'move_group_prefix': 'move_group_prefix1', 'move_group': 'move_group', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1173 y:269
			OperatableStateMachine.add('pickbin6',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'Gripperaan_2', 'planning_failed': 'failed', 'control_failed': 'Retry_2'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'move_group_prefix': 'move_group_prefix1', 'move_group': 'move_group', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1171 y:353
			OperatableStateMachine.add('pickbin1',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'Gripperaan_4', 'planning_failed': 'failed', 'control_failed': 'Retry_3'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'move_group_prefix': 'move_group_prefix2', 'move_group': 'move_group', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1185 y:524
			OperatableStateMachine.add('pickbin2',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'Gripperaan_3', 'planning_failed': 'failed', 'control_failed': 'Retry_4'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'move_group_prefix': 'move_group_prefix2', 'move_group': 'move_group', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1568 y:43
			OperatableStateMachine.add('pregraspbin5_2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'finished', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_bin5PreGrasp', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix1', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1568 y:262
			OperatableStateMachine.add('pregraspbin6_2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'finished', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_bin5PreGrasp', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix1', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1566 y:349
			OperatableStateMachine.add('pregraspbin1_2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'finished', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_bin1PreGrasp', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix2', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1569 y:515
			OperatableStateMachine.add('pregraspbin2_2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'finished', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_bin2PreGrasp', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix2', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1674 y:635
			OperatableStateMachine.add('MoseMessage',
										MessageState(),
										transitions={'continue': 'finished'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'part_pose'})

			# x:818 y:46
			OperatableStateMachine.add('detectpartbin5',
										DetectPartCameraAriacState(time_out=0.5),
										transitions={'continue': 'Computegraspbin5', 'failed': 'failed', 'not_found': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'camera_ref_frame', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'part': 'part_type', 'pose': 'part_pose'})

			# x:1193 y:136
			OperatableStateMachine.add('Retry',
										WaitState(wait_time=1),
										transitions={'done': 'gripperkeuze'},
										autonomy={'done': Autonomy.Off})

			# x:820 y:265
			OperatableStateMachine.add('detectpartbin6',
										DetectPartCameraAriacState(time_out=0.5),
										transitions={'continue': 'Computegraspbin5_2', 'failed': 'failed', 'not_found': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'camera_ref_frame', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'part': 'part_type', 'pose': 'part_pose'})

			# x:820 y:348
			OperatableStateMachine.add('detectpartbin1',
										DetectPartCameraAriacState(time_out=0.5),
										transitions={'continue': 'Computegraspbin5_3', 'failed': 'failed', 'not_found': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'camera_ref_frame', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'part': 'part_type', 'pose': 'part_pose'})

			# x:833 y:530
			OperatableStateMachine.add('detectpartbin2',
										DetectPartCameraAriacState(time_out=0.5),
										transitions={'continue': 'Computegraspbin5_4', 'failed': 'failed', 'not_found': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'camera_ref_frame', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'part': 'part_type', 'pose': 'part_pose'})

			# x:997 y:44
			OperatableStateMachine.add('Computegraspbin5',
										ComputeGraspAriacState(joint_names=['linear_arm_actuator_joint', 'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']),
										transitions={'continue': 'Computegraspbin5', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix1', 'tool_link': 'tool_link', 'pose': 'part_pose', 'offset': 'part_offset', 'rotation': 'part_rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1382 y:37
			OperatableStateMachine.add('Gripperaan',
										VacuumGripperControlState(enable=True),
										transitions={'continue': 'pregraspbin5_2', 'failed': 'failed', 'invalid_arm_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id'})

			# x:1363 y:129
			OperatableStateMachine.add('gripperkeuze',
										ReplaceState(),
										transitions={'done': 'Gripperaan'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'gripper1', 'result': 'arm_id'})

			# x:1000 y:254
			OperatableStateMachine.add('Computegraspbin5_2',
										ComputeGraspAriacState(joint_names=['linear_arm_actuator_joint', 'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']),
										transitions={'continue': 'Computegraspbin5_2', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix1', 'tool_link': 'tool_link', 'pose': 'part_pose', 'offset': 'part_offset', 'rotation': 'part_rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1003 y:346
			OperatableStateMachine.add('Computegraspbin5_3',
										ComputeGraspAriacState(joint_names=['linear_arm_actuator_joint', 'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']),
										transitions={'continue': 'Computegraspbin5_3', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix1', 'tool_link': 'tool_link', 'pose': 'part_pose', 'offset': 'part_offset', 'rotation': 'part_rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1023 y:524
			OperatableStateMachine.add('Computegraspbin5_4',
										ComputeGraspAriacState(joint_names=['linear_arm_actuator_joint', 'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']),
										transitions={'continue': 'Computegraspbin5_4', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix1', 'tool_link': 'tool_link', 'pose': 'part_pose', 'offset': 'part_offset', 'rotation': 'part_rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1193 y:198
			OperatableStateMachine.add('Retry_2',
										WaitState(wait_time=1),
										transitions={'done': 'gripperkeuze_2'},
										autonomy={'done': Autonomy.Off})

			# x:1206 y:434
			OperatableStateMachine.add('Retry_3',
										WaitState(wait_time=1),
										transitions={'done': 'gripperkeuze_3'},
										autonomy={'done': Autonomy.Off})

			# x:1200 y:628
			OperatableStateMachine.add('Retry_4',
										WaitState(wait_time=1),
										transitions={'done': 'gripperkeuze_4'},
										autonomy={'done': Autonomy.Off})

			# x:1362 y:199
			OperatableStateMachine.add('gripperkeuze_2',
										ReplaceState(),
										transitions={'done': 'Gripperaan_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'gripper1', 'result': 'arm_id'})

			# x:1359 y:426
			OperatableStateMachine.add('gripperkeuze_3',
										ReplaceState(),
										transitions={'done': 'Gripperaan_4'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'gripper2', 'result': 'arm_id'})

			# x:1357 y:642
			OperatableStateMachine.add('gripperkeuze_4',
										ReplaceState(),
										transitions={'done': 'Gripperaan_3'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'gripper2', 'result': 'arm_id'})

			# x:1359 y:261
			OperatableStateMachine.add('Gripperaan_2',
										VacuumGripperControlState(enable=True),
										transitions={'continue': 'pregraspbin6_2', 'failed': 'failed', 'invalid_arm_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id'})

			# x:1377 y:511
			OperatableStateMachine.add('Gripperaan_3',
										VacuumGripperControlState(enable=True),
										transitions={'continue': 'pregraspbin2_2', 'failed': 'failed', 'invalid_arm_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id'})

			# x:1362 y:345
			OperatableStateMachine.add('Gripperaan_4',
										VacuumGripperControlState(enable=True),
										transitions={'continue': 'pregraspbin1_2', 'failed': 'failed', 'invalid_arm_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
