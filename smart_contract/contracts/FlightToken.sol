// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract FlightToken is ERC721, ERC721Enumerable, Ownable {
    struct Ticket {
        string customer_name;
        string customer_last_name;
        string departure_city;
        string arrival_city;
        string date_of_purchase;
        string departure_date;
        uint256 price;
        string airplane_code;
        uint256 ticket_code;
    }

    using Counters for Counters.Counter;
    Ticket[] public tickets;

    Counters.Counter private _tokenIdCounter;

    constructor() ERC721("FlightToken", "FLT") {}

    function safeMint(
        string memory _customer_name,
        string memory _customer_last_name,
        string memory _departure_city,
        string memory _arrival_city,
        string memory _date_of_purchase,
        string memory _departure_date,
        uint256 _price,
        string memory _airplane_code
    ) public payable returns (uint256) {
        require(msg.value >= 1 ether, "Not enought ether sent.");
        _tokenIdCounter.increment();

        Ticket memory new_ticket = Ticket({
            customer_name: _customer_name,
            customer_last_name: _customer_last_name,
            departure_city: _departure_city,
            arrival_city: _arrival_city,
            date_of_purchase: _date_of_purchase,
            departure_date: _departure_date,
            price: _price,
            airplane_code: _airplane_code,
            ticket_code: _tokenIdCounter.current()
        });
        tickets.push(new_ticket);
        _safeMint(msg.sender, _tokenIdCounter.current());
        payable(owner()).transfer(address(this).balance);
        return _tokenIdCounter.current();
    }

    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override(ERC721, ERC721Enumerable) {
        require(from == to, "NonTransferrable token");
        super._beforeTokenTransfer(from, to, tokenId);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721Enumerable)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}
