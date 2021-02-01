"""
reworked to abstract loop method

#open dos shell
cmd
d:
cd D:\2020\coding\anne_EC50\robot
opentron_venv\Scripts\activate.bat
opentrons_simulate.exe demo_new_5.py

NB: .mix & .touch steps commented out during code testing
refer "for matthew.ods" for explanation of plates and movements.
#https://docs.opentrons.com/v2/new_complex_commands.html
"""

from opentrons import protocol_api
# metadata
metadata = {
    'protocolName': 'TimTamDemo1',
    'author': 'Matthew <bmatthewtaylor@gmail.com>',
    'description': 'protocol for demo',
    'apiLevel': '2.9'
}

# protocol run function. the part after the colon lets your editor know
# where to look for autocomplete suggestions

def fill_rack(left_pipette, tipracks_, master, destination, control_1, control_2, master_offset_col, dest_name):
    #master_offset_col=0#master_offset_col move to function variables for algo simplicity.
    #dest_cols design does not need to be in function variables for this experiment design.
    dest_cols= [2, 22, 3,23]
    #
    #f.write("start "+dest_name+" ______________________________\n")
    #f.write("master_offset_col:"+str(master_offset_col)+"\n")
    #control1 from col2 to destination col2 and 22.
    for col_pos in dest_cols[0:2]:
        for offset_row in ["A","B"]:
            source_pos = offset_row+str(2)#pickup from control1 col 2
            source = control_1[source_pos]
            well_pos = offset_row+str(col_pos)
            csv_string = source_pos+","+well_pos
            print(csv_string)
            left_pipette.pick_up_tip()
            left_pipette.mix(2, 10)
            left_pipette.transfer(5, source.bottom(2), destination[well_pos].top(-2), new_tip='never')
            left_pipette.touch_tip()   #reinstate .touch step for production
            left_pipette.drop_tip()
            #f.write("control1: "+csv_string+"\n")
    #
    #control2 from col2 to destination col3 and 22.
    for col_pos in dest_cols[2:4]:
        for offset_row in ["A","B"]:
            source_pos = offset_row+str(2)#pickup from control2 col 2
            source = control_2[source_pos]
            well_pos = offset_row+str(col_pos)
            csv_string = source_pos+","+well_pos
            print(csv_string)
            left_pipette.pick_up_tip()#'out of tips' error when on destination plate 2
            left_pipette.mix(2, 10)
            left_pipette.transfer(5, source.bottom(2), destination[well_pos].top(-2), new_tip='never')
            left_pipette.touch_tip()   #reinstate .touch step for production
            left_pipette.drop_tip()
            #f.write("control2: "+csv_string+"\n")
    #
    #in previous simpler algo, pick from col 1 put to cols [4,5,6], then from col 2 to [7,8,9]
    # etc until pick from col 6 put to col [19,20,21]
    #in new algo with 4 destination plates
    # destination plate 2 picks from col 7 put to cols [4,5,6] etc until pick from col 12 put to [19,20,21]
    #need to rework how source and destination columns are calculated.
    #new variable master_offset_col will be
    #0 for destination1, 6 for destination2, 12 for destination3, 18 for destination4
    for col_pos in list(range(0, 6)):
        for offset_row in ["A","B"]:
            #print("source col_pos:", col_pos+1)
            #print("dest col_pos:", col_pos*3+4)
            #print("source pos:", offset_row+str(col_pos+1))
            source_address = offset_row+str(col_pos+1+master_offset_col)
            source = master[source_address]
            #for well_pos in ['A4', 'A5', 'A6']:
            for i in range(0,3):
                #print("dest pos: ", offset_row+str(col_pos*3+4+i))
                well_pos = offset_row+str(col_pos*3+4+i)
                left_pipette.pick_up_tip()
                left_pipette.mix(2, 10)    #reinstate .mix step for production.
                #f.write("destination: "+source_address+","+well_pos+"\n")
                left_pipette.transfer(5, source.bottom(2), destination[well_pos].top(-2), new_tip='never')
                left_pipette.touch_tip()   #reinstate .touch step for production
                left_pipette.drop_tip()
    #
    #f.write("end "+dest_name+" ______________________________\n")


def run(protocol):
    #
    #f = open('transfer_pos_records.csv','w')
    # labware
    microplate_name = 'corning_384_wellplate_112ul_flat'
    master 		= protocol.load_labware(microplate_name, '1')
    destination1 = protocol.load_labware(microplate_name, '2')
    #destination2 = protocol.load_labware(microplate_name, '9')#check position
    #destination3 = protocol.load_labware(microplate_name, '10')#check position
    #destination4 = protocol.load_labware(microplate_name, '11')#check position
    control_1  	= protocol.load_labware(microplate_name, '3')
    control_2 	= protocol.load_labware(microplate_name, '5')
    #
    tipracks_ = [protocol.load_labware('geb_96_tiprack_10ul', str(slot))
            for slot in ['4', '6', '7', '8']]
    #
    left_pipette = protocol.load_instrument('p10_multi', 'left', tip_racks=tipracks_)
    #
    #left_pipette.pick_up_tip()
    # Change default aspirate speed to 50ul/s, 1/3 of the default
    left_pipette.flow_rate.aspirate = 10
    #left_pipette.aspirate(100, plate['A1'])
    # Slow down dispense too
    left_pipette.flow_rate.dispense = 200
    #left_pipette.dispense(100, plate['B2'])
    #left_pipette.drop_tip()
    print("type(master):", type(master))
    print("type(destination1):", type(destination1))
    #print("type(destination2):", type(destination2))
    #print("type(destination3):", type(destination3))
    #print("type(destination4):", type(destination4))
    print("type(control_1):", type(control_1))
    print("type(control_2):", type(control_2))
    print("type(tipracks_):", type(tipracks_))
    print("type(left_pipette):", type(left_pipette))
    #
    print("start dest plate 1")
    fill_rack(left_pipette, tipracks_, master, destination1, control_1, control_2, 0, "Destination plate 1")
    protocol.pause("Put a new plate in slot ?? and refill all of the tipracks.")
    #
    print("start dest plate 2")
    left_pipette.reset_tipracks()
    #fill_rack(left_pipette, tipracks_, master, destination1, control_1, control_2, 6, "Destination plate 2", f)
    fill_rack(left_pipette, tipracks_, master, destination1, control_1, control_2, 6, "Destination plate 2")
    protocol.pause("Put a new plate in slot ?? and refill all of the tipracks.")
    #
    print("start dest plate 3")
    left_pipette.reset_tipracks()
    fill_rack(left_pipette, tipracks_, master, destination1, control_1, control_2, 12, "Destination plate 3")
    protocol.pause("Put a new plate in slot ?? and refill all of the tipracks.")
    #
    print("start dest plate 4")
    left_pipette.reset_tipracks()
    fill_rack(left_pipette, tipracks_, master, destination1, control_1, control_2, 18, "Destination plate 4")
    #
    #f.close()
