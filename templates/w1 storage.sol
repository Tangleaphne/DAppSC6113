// SPDX-License-Identifier: MIT

pragma solidity ^0.8;

contract store_money{
    uint money;

    function store_m(uint num) public {
        money = num;
    }

    function view_m() public view returns (uint) {
        return money;
    }

}