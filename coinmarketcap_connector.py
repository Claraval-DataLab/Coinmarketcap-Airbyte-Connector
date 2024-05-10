version: 0.85.0

type: DeclarativeSource

check:
  type: CheckStream
  stream_names:
    - Coinmarketcap-Airbyte-Connector

definitions:
  streams:
    Coinmarketcap-Airbyte-Connector:
      type: DeclarativeStream
      name: Coinmarketcap-Airbyte-Connector
      retriever:
        type: SimpleRetriever
        requester:
          $ref: '#/definitions/base_requester'
          path: https://web-api.coinmarketcap.com/v1/cryptocurrency/listings/latest
          http_method: GET
        record_selector:
          type: RecordSelector
          extractor:
            type: DpathExtractor
            field_path: []
      incremental_sync:
        type: DatetimeBasedCursor
        cursor_field: created_at
        cursor_datetime_formats:
          - '%Y-%m-%d %H:%M:%S'
        datetime_format: '%Y-%m-%d %H:%M:%S'
        start_datetime:
          type: MinMaxDatetime
          datetime: '{{ config["start_date"] }}'
          datetime_format: '%Y-%m-%dT%H:%M:%SZ'
        start_time_option:
          type: RequestOption
          inject_into: request_parameter
        end_time_option:
          type: RequestOption
          inject_into: request_parameter
        end_datetime:
          type: MinMaxDatetime
          datetime: '{{ now_utc().strftime(''%Y-%m-%dT%H:%M:%SZ'') }}'
          datetime_format: '%Y-%m-%dT%H:%M:%SZ'
      schema_loader:
        type: InlineSchemaLoader
        schema:
          $ref: '#/schemas/Coinmarketcap-Airbyte-Connector'
  base_requester:
    type: HttpRequester
    url_base: https://web-api.coinmarketcap.com/v1/cryptocurrency/listings/latest

streams:
  - $ref: '#/definitions/streams/Coinmarketcap-Airbyte-Connector'

spec:
  type: Spec
  connection_specification:
    type: object
    $schema: http://json-schema.org/draft-07/schema#
    required:
      - start_date
    properties:
      start_date:
        type: string
        title: Start date
        format: date-time
        pattern: ^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$
        order: 0
    additionalProperties: true

metadata:
  autoImportSchema:
    Coinmarketcap-Airbyte-Connector: true

schemas:
  Coinmarketcap-Airbyte-Connector:
    type: object
    $schema: http://json-schema.org/schema#
    additionalProperties: true
    properties:
      data:
        type:
          - array
          - 'null'
        items:
          type:
            - object
            - 'null'
          properties:
            circulating_supply:
              type:
                - number
                - 'null'
            cmc_rank:
              type:
                - number
                - 'null'
            date_added:
              type:
                - string
                - 'null'
            id:
              type:
                - number
                - 'null'
            infinite_supply:
              type:
                - boolean
                - 'null'
            last_updated:
              type:
                - string
                - 'null'
            max_supply:
              type:
                - number
                - 'null'
            name:
              type:
                - string
                - 'null'
            num_market_pairs:
              type:
                - number
                - 'null'
            platform:
              type:
                - object
                - 'null'
              properties:
                id:
                  type:
                    - number
                    - 'null'
                name:
                  type:
                    - string
                    - 'null'
                slug:
                  type:
                    - string
                    - 'null'
                symbol:
                  type:
                    - string
                    - 'null'
                token_address:
                  type:
                    - string
                    - 'null'
            quote:
              type:
                - object
                - 'null'
              properties:
                USD:
                  type:
                    - object
                    - 'null'
                  properties:
                    fully_diluted_market_cap:
                      type:
                        - number
                        - 'null'
                    last_updated:
                      type:
                        - string
                        - 'null'
                    market_cap:
                      type:
                        - number
                        - 'null'
                    market_cap_dominance:
                      type:
                        - number
                        - 'null'
                    percent_change_1h:
                      type:
                        - number
                        - 'null'
                    percent_change_24h:
                      type:
                        - number
                        - 'null'
                    percent_change_30d:
                      type:
                        - number
                        - 'null'
                    percent_change_60d:
                      type:
                        - number
                        - 'null'
                    percent_change_7d:
                      type:
                        - number
                        - 'null'
                    percent_change_90d:
                      type:
                        - number
                        - 'null'
                    price:
                      type:
                        - number
                        - 'null'
                    tvl:
                      type:
                        - number
                        - 'null'
                    volume_24h:
                      type:
                        - number
                        - 'null'
                    volume_change_24h:
                      type:
                        - number
                        - 'null'
            self_reported_circulating_supply:
              type:
                - number
                - 'null'
            self_reported_market_cap:
              type:
                - number
                - 'null'
            slug:
              type:
                - string
                - 'null'
            symbol:
              type:
                - string
                - 'null'
            tags:
              type:
                - array
                - 'null'
              items:
                type:
                  - string
                  - 'null'
            total_supply:
              type:
                - number
                - 'null'
            tvl_ratio:
              type:
                - number
                - 'null'
      status:
        type:
          - object
          - 'null'
        properties:
          credit_count:
            type:
              - number
              - 'null'
          elapsed:
            type:
              - number
              - 'null'
          error_code:
            type:
              - number
              - 'null'
          timestamp:
            type:
              - string
              - 'null'
          total_count:
            type:
              - number
              - 'null'
