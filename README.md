# Ethereum CEX-DEX transaction dataset 
A dataset (sample) of CEX-DEX transactions on the Ethereum mainnet identified by a set of heuristics implemented on Dune Analytics, including the information of the block, the transaction, and the DEX trade(s) executed by the transaction. 

A Python script for parsing CEX token price data from [Tardis](https://docs.tardis.dev/downloadable-csv-files#trades) is also provided. 

The dataset is curated by [Fei](https://x.com/William33203632) and [Danning](https://x.com/sui414), and is part of the [TLDR 2024 fellowship program](https://www.thelatestindefi.org/fellowships).

## About the dataset

**date_range:** `2023-08-08 to 2025-03-08`

**size:** `~4 GB` for the entire time range.

**structure:** `[8721772, 21]` (8,721,772 rows, 21 columns)

**source:** Dune

**blockchain:** Ethereum

**variables:**

| Variable                | Type     | Description                                                  |
| ----------------------- | -------- | ------------------------------------------------------------ |
| `block_number`          | INT      | Block number                                                 |
| `block_time`            | DATETIME | UTC timestamp of the block                                   |
| `tx_hash`               | VARCHAR  | Transaction Hash                                             |
| `tx_index`              | INT      | Index of the transaction within the block                    |
| `from_addr`             | VARCHAR  | Address sending the transaction                              |
| `to_addr`               | VARCHAR  | Address receiving the transaction                            |
| `mev_bot_label`         | VARCHAR  | Label identifying the MEV bot (if applicable)                |
| `base_fees`             | FLOAT    | Base fees paid for the transaction                           |
| `priority_fees`         | FLOAT    | Tips or priority fees paid to the builder                    |
| `cb_transfer`           | FLOAT    | Coinbase transfer paid to the builder                        |
| `mev_value`             | FLOAT    | priority_fees + cb_transfer                                  |
| `volume`                | FLOAT    | USD notional volume of the trade                             |
| `token_bought_amount`   | FLOAT    | Amount of token bought                                       |
| `token_sold_amount`     | FLOAT    | Amount of token sold                                         |
| `token_bought_contract` | VARCHAR  | ERC-20 contract address of the token bought                  |
| `token_sold_contract`   | VARCHAR  | ERC-20 contract address of the token sold                    |
| `token_bought_symbol`   | VARCHAR  | Symbol of the token bought                                   |
| `token_sold_symbol`     | VARCHAR  | Symbol of the token sold                                     |
| `pair`                  | VARCHAR  | Token trading pair                                           |
| `multi_trade`           | INT      | Flag indicating if the trade includes multiple swaps (0 or 1) |
| `builder_label`         | VARCHAR  | Builder of the block identified by extra_data                |

**other_notes:** Transactions with identifiable MEV bot interactions are labeled. Dataset may include rows with `<nil>` in MEV bot label.
