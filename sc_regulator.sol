// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.4.0 <0.9.0;

contract pharma_aproval {   
    string description;
    string sku;
    string category;
    string public regulator;
    string date;

   function info() public 
   {
    regulator = 'Approved';
    sku = 'KS944RUR';
    description = 'VIDACOM234';
    category = 'Anti Depressive';
    date = '20220422';
    }

    function get() view public returns (string memory) 
    {
        return regulator;
    }

}   
