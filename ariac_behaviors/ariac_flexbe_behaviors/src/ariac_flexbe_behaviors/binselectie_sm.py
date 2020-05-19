#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_support_flexbe_states.equal_state import EqualState
from ariac_support_flexbe_states.replace_state import ReplaceState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Fri May 15 2020
@author: Bas
'''
class binSelectieSM(Behavior):
	'''
	bin selectie en camera selectie bij bin.
	'''


	def __init__(self):
		super(binSelectieSM, self).__init__()
		self.name = 'binSelectie'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1169 y:86, x:82 y:552
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['part_type'], output_keys=['camera_topic', 'camera_ref_frame', 'camera_frame', 'part_offset'])
		_state_machine.userdata.part_type = ''
		_state_machine.userdata.part1 = 'gear_part'
		_state_machine.userdata.part2 = 'piston_rod_part'
		_state_machine.userdata.part3 = 'pully_part'
		_state_machine.userdata.part4 = 'gasket_part'
		_state_machine.userdata.move_group_prefix1 = 'ariac/arm1'
		_state_machine.userdata.move_group_prefix2 = 'ariac/arm2'
		_state_machine.userdata.camera_ref_frame = ''
		_state_machine.userdata.camera_ref_frame1 = 'arm1_linear_arm_actuator'
		_state_machine.userdata.camera_topic = ''
		_state_machine.userdata.camera_frame1 = 'logical_camera_1_frame'
		_state_machine.userdata.camera_ref_frame2 = 'arm2_linear_arm_actuator'
		_state_machine.userdata.camera_topic2 = '/ariac/logical_camera_2'
		_state_machine.userdata.camera_topic3 = '/ariac/logical_camera_3'
		_state_machine.userdata.camera_topic4 = '/ariac/logical_camera_4'
		_state_machine.userdata.camera_topic1 = '/ariac/logical_camera_1'
		_state_machine.userdata.camera_frame2 = 'logical_camera_2_frame'
		_state_machine.userdata.camera_frame3 = 'logical_camera_3_frame'
		_state_machine.userdata.camera_frame4 = 'logical_camera_4_frame'
		_state_machine.userdata.camera_frame = ''
		_state_machine.userdata.part_offset = 0
		_state_machine.userdata.offset1 = 0
		_state_machine.userdata.offset2 = 0
		_state_machine.userdata.offset3 = 0
		_state_machine.userdata.offset4 = 0
		_state_machine.userdata.tool_link = 'ee_link'

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:131 y:69
			OperatableStateMachine.add('partselectie1',
										EqualState(),
										transitions={'true': 'camerarefframe1', 'false': 'partselectie2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'part_type', 'value_b': 'part1'})

			# x:129 y:184
			OperatableStateMachine.add('partselectie2',
										EqualState(),
										transitions={'true': 'camerarefframe1_2', 'false': 'partselectie3'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'part_type', 'value_b': 'part2'})

			# x:127 y:309
			OperatableStateMachine.add('partselectie3',
										EqualState(),
										transitions={'true': 'camerarefframe1_3', 'false': 'partselectie4'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'part_type', 'value_b': 'part3'})

			# x:126 y:425
			OperatableStateMachine.add('partselectie4',
										EqualState(),
										transitions={'true': 'camerarefframe1_4', 'false': 'failed'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'part_type', 'value_b': 'part4'})

			# x:315 y:64
			OperatableStateMachine.add('camerarefframe1',
										ReplaceState(),
										transitions={'done': 'camerarefframe1_5'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'camera_ref_frame1', 'result': 'camera_ref_frame'})

			# x:306 y:177
			OperatableStateMachine.add('camerarefframe1_2',
										ReplaceState(),
										transitions={'done': 'camerarefframe1_6'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'camera_ref_frame1', 'result': 'camera_ref_frame'})

			# x:307 y:293
			OperatableStateMachine.add('camerarefframe1_3',
										ReplaceState(),
										transitions={'done': 'camerarefframe1_7'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'camera_ref_frame2', 'result': 'camera_ref_frame'})

			# x:306 y:408
			OperatableStateMachine.add('camerarefframe1_4',
										ReplaceState(),
										transitions={'done': 'camerarefframe1_8'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'camera_ref_frame2', 'result': 'camera_ref_frame'})

			# x:486 y:64
			OperatableStateMachine.add('camerarefframe1_5',
										ReplaceState(),
										transitions={'done': 'camerarefframe1_9'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'camera_topic1', 'result': 'camera_topic'})

			# x:477 y:177
			OperatableStateMachine.add('camerarefframe1_6',
										ReplaceState(),
										transitions={'done': 'camerarefframe1_10'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'camera_topic2', 'result': 'camera_topic'})

			# x:480 y:294
			OperatableStateMachine.add('camerarefframe1_7',
										ReplaceState(),
										transitions={'done': 'camerarefframe1_11'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'camera_topic3', 'result': 'camera_topic'})

			# x:480 y:406
			OperatableStateMachine.add('camerarefframe1_8',
										ReplaceState(),
										transitions={'done': 'camerarefframe1_12'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'camera_topic4', 'result': 'camera_topic'})

			# x:666 y:60
			OperatableStateMachine.add('camerarefframe1_9',
										ReplaceState(),
										transitions={'done': 'offsetgearpart'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'camera_frame1', 'result': 'camera_frame'})

			# x:660 y:179
			OperatableStateMachine.add('camerarefframe1_10',
										ReplaceState(),
										transitions={'done': 'offsetPistonrodpart'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'camera_frame2', 'result': 'camera_frame'})

			# x:666 y:289
			OperatableStateMachine.add('camerarefframe1_11',
										ReplaceState(),
										transitions={'done': 'offsetpullypart'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'camera_frame3', 'result': 'camera_frame'})

			# x:671 y:398
			OperatableStateMachine.add('camerarefframe1_12',
										ReplaceState(),
										transitions={'done': 'offsetGasketpart'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'camera_frame4', 'result': 'camera_frame'})

			# x:852 y:58
			OperatableStateMachine.add('offsetgearpart',
										ReplaceState(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'offset1', 'result': 'part_offset'})

			# x:854 y:178
			OperatableStateMachine.add('offsetPistonrodpart',
										ReplaceState(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'offset2', 'result': 'part_offset'})

			# x:860 y:287
			OperatableStateMachine.add('offsetpullypart',
										ReplaceState(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'offset3', 'result': 'part_offset'})

			# x:864 y:395
			OperatableStateMachine.add('offsetGasketpart',
										ReplaceState(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'offset4', 'result': 'part_offset'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
