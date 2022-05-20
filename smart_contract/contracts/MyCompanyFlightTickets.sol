// SPDX-License-Identifier: MIT
pragma solidity >=0.8.7;

contract MyCompanyFlightTickets {
    struct Ticket {
        string customer_name;
        string customer_last_name;
        string departure_city;
        string arrival_city;
        string date_of_purchase;
        string departure_date;
        uint256 price;
        string airplane_code;
        string ticket_code;
    }

    Ticket[] public tickets;
    mapping(string => Ticket) public ticketCodeToTicked;
    address public owner;

    constructor() {
        owner = msg.sender;
        tickets.push(Ticket("Filippo", "Gabriele","0","0", "0", "0", 0, "0", "0"));
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can add players");
        _;
    }

    function addTicket(string memory _customer_name, 
    string memory _customer_last_name,
    string memory _departure_city,
    string memory _arrival_city,
    string memory _date_of_purchase,
    string memory _departure_date,
    uint256 _price,
    string memory _airplane_code,
    string memory _ticket_code
    ) public onlyOwner {
        Ticket memory new_ticket = Ticket({
            customer_name: _customer_name,
            customer_last_name: _customer_last_name,
            departure_city: _departure_city,
            arrival_city: _arrival_city,
            date_of_purchase: _date_of_purchase,
            departure_date: _departure_date,
            price: _price,
            airplane_code: _airplane_code,
            ticket_code: _ticket_code
        });
        tickets.push(new_ticket);
        ticketCodeToTicked[_ticket_code] = new_ticket;
    }

    function getAllTickets() public view returns (Ticket[] memory) {
        return tickets;
    }

    function getTicketFromCode(string memory _ticket_code) public view returns(Ticket memory){
        return ticketCodeToTicked[_ticket_code];
    }

    function returnFirstTicket() public view returns (Ticket memory) {
        return tickets[0];
    }
}
