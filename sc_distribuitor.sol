// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.4.0 <0.9.0;

contract distribuition { 
    string remetente;
    string destinatario;
    string distribuitionID;  
    string hssCode;
    string IoTDeviceTemp;
    string IotDeviceHumidity;
    string distribuitionDate;
    string status;

   function info() public 
   {
    remetente = 'Hospital';
    destinatario = 'Manufacturer';
    distribuitionID = '09waFgsa';  
    hssCode = 'H35123679';
    IoTDeviceTemp = '-5';
    IotDeviceHumidity = '2';
    distribuitionDate = '20220425';
    status = '';
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
