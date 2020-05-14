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
Created on Thu May 14 2020
@author: Bas
'''
class RobotSelectorStateSM(Behavior):
	'''
	selecteren van de juiste robot
	'''


	def __init__(self):
		super(RobotSelectorStateSM, self).__init__()
		self.name = 'RobotSelectorState'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:533 y:79, x:130 y:365
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['arm_id'], output_keys=['move_group_prefix'])
		_state_machine.userdata.prefix_arm1 = 'ariac/arm1'
		_state_machine.userdata.prefix_arm2 = 'ariac/arm2'
		_state_machine.userdata.arm1 = 'arm1'
		_state_machine.userdata.arm2 = 'arm2'
		_state_machine.userdata.arm_id = ''
		_state_machine.userdata.move_group_prefix = ''

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:51 y:45
			OperatableStateMachine.add('vergelijk1',
										EqualState(),
										transitions={'true': 'value1', 'false': 'vergelijk1_2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'arm_id', 'value_b': 'arm1'})

			# x:50 y:168
			OperatableStateMachine.add('vergelijk1_2',
										EqualState(),
										transitions={'true': 'value1_2', 'false': 'failed'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'arm_id', 'value_b': 'arm2'})

			# x:280 y:49
			OperatableStateMachine.add('value1',
										ReplaceState(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'prefix_arm1', 'result': 'move_group_prefix'})

			# x:279 y:169
			OperatableStateMachine.add('value1_2',
										ReplaceState(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'prefix_arm2', 'result': 'move_group_prefix'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
