const FlightRomeNYNFT = artifacts.require("FlightRomeNYNFT");


contract("FlightRomeNYNFT", accounts => {
    it("owner should be account[0]", async () => {
        let instance = await FlightRomeNYNFT.deployed();
        let owner = await instance.owner();
        assert.equal(owner, accounts[0]);
    })

    it("the last id", async () => {
        let instance = await FlightRomeNYNFT.deployed();
        let id = await instance.returnLastId();
        assert.equal(id < 100, id);
    })
})
