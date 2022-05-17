// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.4.0 <0.9.0;

contract pharma {   
    string description;
    string sku;
    string category;
    string IoTDeviceTemp;
    string IotDeviceHumidity;
    string productionDate;

   function info() public 
   {
    sku = 'KS944RUR';
    description = 'VIDACOM234';
    category = 'Anti Depressive';
    IoTDeviceTemp = '-5';
    IotDeviceHumidity = '2';
    productionDate = '20220422';
    }

    function getIoTDeviceTemp() view public returns (string memory) 
    {
        return IoTDeviceTemp;
    }
    
    function getIotDeviceHumidity() view public returns (string memory) 
    {
        return IotDeviceHumidity;
    }

}   
