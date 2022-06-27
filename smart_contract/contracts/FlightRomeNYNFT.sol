// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract FlightRomeNYNFT is ERC721, ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    uint256 public constant maxSupply = 100;
    Counters.Counter private _tokenIdCounter;
    event TicketBought(address _from, address _to, uint256 _id);

    constructor() ERC721("FlightRomeNYNFT", "FRM") {}

    function safeMint() public payable returns (uint256) {
        require(totalSupply() < maxSupply, "Rome-NY Airplane is full");
        require(msg.value == 1 ether, "Not enought ether sent.");
        _tokenIdCounter.increment();
        uint256 id = _tokenIdCounter.current();
        _safeMint(msg.sender, id);
        payable(owner()).transfer(msg.value);
        emit TicketBought(msg.sender, owner(), id);
        return id;
    }

    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override(ERC721, ERC721Enumerable) {
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

    function returnLastId() public view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
