#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.start_assignment_state import StartAssignment
from ariac_logistics_flexbe_states.get_order_state import GetOrderState
from ariac_logistics_flexbe_states.get_products_from_shipment_state import GetProductsFromShipmentState
from ariac_logistics_flexbe_states.get_part_from_products_state import GetPartFromProductsState
from ariac_support_flexbe_states.add_numeric_state import AddNumericState
from ariac_support_flexbe_states.equal_state import EqualState
from ariac_flexbe_behaviors.transport_part_form_bin_to_agv_state_sm import transport_part_form_bin_to_agv_stateSM
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu May 14 2020
@author: Youp de Haas
'''
class Wrapup_voorbeeld_order_handelingSM(Behavior):
	'''
	Voorbeeld uit wrapup over het verwerken van
	'''


	def __init__(self):
		super(Wrapup_voorbeeld_order_handelingSM, self).__init__()
		self.name = 'Wrapup_voorbeeld_order_handeling'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(transport_part_form_bin_to_agv_stateSM, 'transport_part_form_bin_to_agv_state')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:642 y:425, x:506 y:337
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.order_id = ' '
		_state_machine.userdata.shipments = []
		_state_machine.userdata.number_of_shipments = 0
		_state_machine.userdata.shipment_index = 0
		_state_machine.userdata.shipment_type = ''
		_state_machine.userdata.agv_id = ''
		_state_machine.userdata.products = []
		_state_machine.userdata.number_of_products = 0
		_state_machine.userdata.product_index = 0
		_state_machine.userdata.part_type = ''
		_state_machine.userdata.part_pose = ''
		_state_machine.userdata.one_value = 1
		_state_machine.userdata.zero_value = 0

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:59 y:52
			OperatableStateMachine.add('StartAssignment',
										StartAssignment(),
										transitions={'continue': 'GetOrder'},
										autonomy={'continue': Autonomy.Off})

			# x:225 y:52
			OperatableStateMachine.add('GetOrder',
										GetOrderState(),
										transitions={'continue': 'GetProductsFromShipment'},
										autonomy={'continue': Autonomy.Off},
										remapping={'order_id': 'order_id', 'shipments': 'shipments', 'number_of_shipments': 'number_of_shipments'})

			# x:442 y:53
			OperatableStateMachine.add('GetProductsFromShipment',
										GetProductsFromShipmentState(),
										transitions={'continue': 'GetPartFromProduct', 'invalid_index': 'failed'},
										autonomy={'continue': Autonomy.Off, 'invalid_index': Autonomy.Off},
										remapping={'shipments': 'shipments', 'index': 'shipment_index', 'shipment_type': 'shipment_type', 'agv_id': 'agv_id', 'products': 'products', 'number_of_products': 'number_of_products'})

			# x:675 y:55
			OperatableStateMachine.add('GetPartFromProduct',
										GetPartFromProductsState(),
										transitions={'continue': 'transport_part_form_bin_to_agv_state', 'invalid_index': 'failed'},
										autonomy={'continue': Autonomy.Off, 'invalid_index': Autonomy.Off},
										remapping={'products': 'products', 'index': 'product_index', 'type': 'part_type', 'pose': 'Part_pose'})

			# x:958 y:176
			OperatableStateMachine.add('IncrementProductIndex',
										AddNumericState(),
										transitions={'done': 'EindeProductenLijst'},
										autonomy={'done': Autonomy.Off},
										remapping={'value_a': 'product_index', 'value_b': 'one_value', 'result': 'product_index'})

			# x:963 y:273
			OperatableStateMachine.add('EindeProductenLijst',
										EqualState(),
										transitions={'true': 'IncrementShipmentIndex', 'false': 'GetPartFromProduct'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'product_index', 'value_b': 'number_of_products'})

			# x:964 y:363
			OperatableStateMachine.add('IncrementShipmentIndex',
										AddNumericState(),
										transitions={'done': 'EindeShipment'},
										autonomy={'done': Autonomy.Off},
										remapping={'value_a': 'shipment_index', 'value_b': 'one_value', 'result': 'shipment_index'})

			# x:967 y:449
			OperatableStateMachine.add('EindeShipment',
										EqualState(),
										transitions={'true': 'GetOrder', 'false': 'GetProductsFromShipment'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'shipment_index', 'value_b': 'number_of_shipments'})

			# x:917 y:45
			OperatableStateMachine.add('transport_part_form_bin_to_agv_state',
										self.use_behavior(transport_part_form_bin_to_agv_stateSM, 'transport_part_form_bin_to_agv_state'),
										transitions={'finished': 'IncrementProductIndex', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'part_type': 'part_type', 'agv_id': 'agv_id', 'pose_on_agv': 'part_pose'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
