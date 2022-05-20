const MyCompanyFlightTickets = artifacts.require("MyCompanyFlightTickets");

module.exports = function (deployer) {
  deployer.deploy(MyCompanyFlightTickets);
};
