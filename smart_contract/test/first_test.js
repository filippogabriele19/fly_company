const MyCompanyFlightTickets = artifacts.require("MyCompanyFlightTickets");


contract("MyCompanyFlightTickets", accounts => {
    it("owner should be account[0]", async () => {
        let instance = await MyCompanyFlightTickets.deployed();
        let owner = await instance.owner();
        assert.equal(owner, accounts[0]);
    })

    it("the first ticket should be of Filippo", async () => {
        let instance = await MyCompanyFlightTickets.deployed();
        let first_ticket = await instance.returnFirstTicket();
        assert.equal(first_ticket.customer_name, "Filippo");
    })
})
