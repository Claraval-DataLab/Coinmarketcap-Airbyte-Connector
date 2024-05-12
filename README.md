# Coinmarketcap-Airbyte-Connector

This connector allows you to import data from the CoinMarketCap public API into Airbyte. You can create your own connector in Airbyte using the provided YAML file.

## Usage

To use this connector, follow these steps:

1. Download the `coinmarketcap_airbyte_connector.yaml` file from this repository to your local machine.

2. Import the connector into Airbyte:
   - Open Airbyte in your web browser.
   - Go to the "Builder" tab and click on "Create a new custom connector."
   - Choose "Import a YAML manifest" and select the `coinmarketcap_airbyte_connector.yaml` file you downloaded.
   - Follow the prompts to configure the connector settings, such as API keys and data syncing frequency.
   - Save the connector configuration.

3. Test the connector:
   - Once the connector is configured, you can test it by running a sync in Airbyte.
   - Check the sync logs to ensure that data is being imported correctly from CoinMarketCap.

For more detailed instructions on creating custom connectors in Airbyte, refer to the [Airbyte Connector Builder UI tutorial](https://docs.airbyte.com/connector-development/connector-builder-ui/tutorial).

**Thank you for using the Coinmarketcap-Airbyte-Connector!**

If you have any questions or feedback, please feel free to reach out to me on [GitHub](https://github.com/diegogarcia-claravaldatalab).
