#!/usr/bin/env python
# Example 2-11 Line items from a flat-file invoice

invoice = """
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz01234567890
|-..-||-..............................-||-........-||-||-....-|
1909  Pimoroni PiBrella                       $17.50  3  $52.50
1489  6mm Tactile Switch x20                   $4.95  2   $9.90
1510  Panavise Jr. - PV-201                   $28.00  1  $28.00
1601  PiTFT Mini Kit 320x240                  $34.95  1  $34.95       
"""

SKU = slice(0, 6)
type(SKU)
# Out[12]: slice

DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')    # [2:]
for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])

# opqrstuvwxyz GHIJKLMNOPQRSTUVWXYZabcdefghijklmn
# |-........-| |-..............................-|
#       $17.50 Pimoroni PiBrella
#        $4.95 6mm Tactile Switch x20
#       $28.00 Panavise Jr. - PV-201             
#       $34.95 PiTFT Mini Kit 320x240