const FlightToken = artifacts.require("FlightToken");

module.exports = function (deployer) {
  deployer.deploy(FlightToken);
};
