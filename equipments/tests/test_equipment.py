import pytest
from partners.models import Partner
from equipments.models import Equipment
from equipments.models import AvailableEquipment
from equipments.models import BorrowedEquipment
from equipments.models import BrokenEquipment


@pytest.mark.django_db
class TestEquipments:

    def setup(self):
        self.equipment = Equipment()
        self.partner = Partner(name='partner')
        self.equipment.save()
        self.partner.save()
    
    def test_borrow_equipment_get(self,client):
        response = client.get('equipment/borrow_equipment/', follow=True)
        response.status_code == 200

    def test_list_equipment_get(self,client):
        response = client.get('equipment/list_equipment/', follow=True)
        response.status_code == 200

    def test_register_equipment_get(self,client):
        response = client.get('equipment/registerequipment/', follow=True)
        response.status_code == 200

    def test_register_equipment_post(self,client):
        response = client.post('equipment/registerequipment/',{
            'equipment_name':'test_equipment',
        },follow=True)
        response.status_code == 200

        
    def test_equipment(self,client):
        response = client.get('equipment/borrow_equipment/', follow=True)
        response.status_code == 200
    

    def test_list_equipment(self,client):
        response = client.get('equipment/list_equipment/', follow=True)
        response.status_code == 200
        
    def test_equipment_states(self):

        self.equipment.start_state()
        self.equipment.borrow_equipment(self.partner)
        assert(type(self.equipment.state) == type(BorrowedEquipment()))
        assert(self.equipment.state.partner == self.partner)

        self.equipment.take_back_equipment()
        assert(type(self.equipment.state) == type(AvailableEquipment()))

        self.equipment.disable_equipment()
        assert(type(self.equipment.state) == type(BrokenEquipment()))

        self.equipment.fix_equipment()
        assert(type(self.equipment.state) == type(AvailableEquipment()))
