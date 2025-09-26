import math
import pytest
from typing import List
from transports import Car, Track
from vehicle import Vehicle

class TestTransports:    
    @pytest.fixture(autouse=True)
    def setup_test(self):
        self.car = Car(7)
        self.track = Track(15, 2)
        self.transports: List[Vehicle] = [self.car, self.track]

    def test_transport_fill_up(self):
        for transport in self.transports:
            current_fuel_before_fill_up = transport.remaining_fuel()
            
            liters = 200
            transport.fill_up(liters)
            
            assert transport.remaining_fuel() == current_fuel_before_fill_up + liters

    def test_transport_drive_success(self):
        distance = 100.0
        liters = 300
        
        for transport in self.transports:
            transport.fill_up(liters)
            current_fuel_before_drive = transport.remaining_fuel()
            expected_fuel_consumption = distance / 100 * transport.fuel_consumption_per_100km
            if isinstance(transport, Track):
              expected_fuel_consumption *=transport.trailers

            transport.drive(distance)

            assert math.isclose(current_fuel_before_drive - transport.remaining_fuel(), expected_fuel_consumption, rel_tol=1e-9)

    def test_transport_drive_error(self):      
        for transport in self.transports:
            transport.fill_up(10)
            
            with pytest.raises(ValueError) as exc:
                transport.drive(1000.0)
            
            assert "Недостаточно топлива" in str(exc.value)
          
    def test_transport_remaining_fuel_on_error(self):    
        for transport in self.transports:
            transport.fill_up(5)
            current_fuel_before_drive = transport.remaining_fuel()

            with pytest.raises(ValueError):
                transport.drive(1000.0)

            assert transport.remaining_fuel() == current_fuel_before_drive
            
      
          
      
  