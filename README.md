# POS Invoice Ticket Configuration

**Version:** 1.0.0  
**Author:** Cositt Technology  
**License:** LGPL-3  
**Category:** Sales/Point of Sale

## Overview

This module provides comprehensive customization of the post-payment receipt/invoice display in Odoo Point of Sale for restaurant environments. It enhances receipt readability and intelligently manages payment method information and invoice QR codes based on payment type.

The module is optimized for thermal printers (80mm) commonly used in restaurants and retail, ensuring excellent legibility and professional presentation.

## Features

### Receipt Display Enhancements

- **Payment Method Label:** Clear "Payment Method:" header displays above payment information
- **Enhanced Typography:** Increased font sizes for all critical receipt elements:
  - Total amount (1.35em)
  - Payment lines (1.15em with font weight)
  - Tax/VAT information (1.1em)
  - Change amount (1.1em)
- **Thermal Printer Optimization:** Formatted specifically for 80mm thermal printers with proper spacing and readability

### Payment Method Detection

- **Automatic Payment Type Recognition:** Detects whether payment is cash, card, or mixed
- **Conditional QR Code Display:** Invoice QR code only appears when payment is 100% card-based
- **Smart Payment Labeling:** Displays payment method details in an easy-to-read format

### Technical Integration

- Uses Odoo's native `is_cash_count` payment method property
- Seamlessly integrates with POS Restaurant module
- Compatible with Odoo 19 Enterprise Point of Sale

## Installation

1. Place the module in your Odoo addons directory:
   ```bash
   cp -r cs_pos_invoice_ticket /path/to/odoo/addons/
   ```

2. Update the module list:
   - Navigate to **Apps** > **Update Apps List**
   - Search for "POS Invoice Ticket Configuration"

3. Install the module:
   - Click **Install** on the module card

## Configuration

### Prerequisites

- Point of Sale module must be installed
- POS Restaurant module should be installed for full functionality
- Receipt printer configured in POS settings

### Settings

1. Go to **Point of Sale > Configuration > Point of Sale**
2. Select your POS terminal configuration
3. Ensure the following are configured:
   - **Receipt Printer:** Connected and configured
   - **Payment Methods:** At least one payment method configured
   - **QR Code on Receipts:** (Optional) Enable if you want invoice QR codes
4. Save the configuration

### Payment Methods Setup

1. Navigate to **Point of Sale > Configuration > Payment Methods**
2. For each payment method, configure:
   - **Name:** Payment method name (e.g., "Cash", "Card")
   - **Type:** Select appropriate type
   - **Is Cash Count:** 
     - Check for **cash** payments
     - Uncheck for **card/bank** payments

## Usage

### Receipt Display

When a payment is completed:

1. **Payment Method Section** displays with clear labeling
2. **Payment Details** show in enlarged, readable format
3. **Taxes/IVA** displayed prominently
4. **Change** (if applicable) shown clearly

### Invoice QR Code Behavior

**Scenario 1: 100% Card Payment**
- Invoice QR code is **displayed**
- Customer can scan for digital receipt

**Scenario 2: 100% Cash Payment**
- Invoice QR code is **hidden**
- Receipt shows payment method clearly

**Scenario 3: Mixed Payment (Cash + Card)**
- Invoice QR code is **hidden**
- Both payment methods displayed with amounts

### Thermal Printer Best Practices

1. **Paper Width:** Use 80mm thermal paper
2. **Text Alignment:** Content is center-aligned for professional appearance
3. **Font Sizes:** Automatically optimized for thermal printer output
4. **Logo/Header:** POS header and footer print as configured in POS settings

## Technical Details

### Dependencies

- `point_of_sale` (Odoo core module)
- `pos_restaurant` (Odoo core module)

### Module Components

#### 1. XML Template Override (`order_receipt.xml`)

Inherits from `point_of_sale.OrderReceipt` with two modifications:

- **Payment Label:** Adds "Método de pago:" header before payment lines
- **QR Code Condition:** Adds intelligent `isCardOnlyPayment()` check to QR display

#### 2. JavaScript Patch (`order_receipt.js`)

```javascript
isCardOnlyPayment() {
  // Returns true if ALL payments are card-based (not cash)
  // is_cash_count = true  → cash payment
  // is_cash_count = false → card/bank payment
}
```

#### 3. Styling (`receipt.scss`)

Responsive styling rules for:
- Enhanced typography throughout receipt
- Payment method label formatting
- QR code and portal URL readability
- Tax/VAT section layout

### Key Implementation Details

- **Payment Detection:** Uses `is_cash_count` property on payment methods
- **Conditional Rendering:** QR code visibility based on `isCardOnlyPayment()` function
- **Responsive Design:** Scales appropriately for 80mm thermal printers
- **No Database Changes:** Pure UI customization via template inheritance

## Troubleshooting

### Payment Method Not Displaying

**Problem:** Payment method information is not shown on receipt.

**Solution:**
1. Verify that at least one payment method is configured
2. Check that payment was successfully recorded
3. Ensure POS configuration is saved
4. Clear POS cache and refresh

### QR Code Always Hidden

**Problem:** QR code never appears even with card payments.

**Solution:**
1. Verify **"Receipt QR Code"** is enabled in POS settings:
   - Go to **Point of Sale Configuration > Receipt QR Code**
2. Check that card payment methods have `is_cash_count = false`
3. Ensure the order was finalized with complete card payment
4. Restart POS terminal

### Text Too Small on Receipt

**Problem:** Receipt text is difficult to read on thermal printer.

**Solution:**
1. Verify thermal printer is 80mm width
2. Check printer driver is correctly installed
3. Test printer directly (outside POS)
4. Adjust SCSS values in `receipt.scss` if needed
5. Contact support for custom scaling

### Mixed Payment Not Showing Correctly

**Problem:** Mixed cash/card payments not displaying properly.

**Solution:**
1. Verify all payment methods are configured correctly
2. Ensure both payment lines are recorded in the order
3. Check that payment methods have correct `is_cash_count` values
4. Review the receipt XML template for xpath correctness

## Support

For issues, feature requests, or technical assistance:
- **Website:** https://cositt.com
- **Email:** support@cositt.com

## Compatibility

- **Odoo Version:** 19.0 Enterprise
- **Printer Type:** 80mm Thermal Printers
- **Payment Types:** Cash, Card, Bank Transfer, Mixed

## License

This module is licensed under LGPL-3. See LICENSE file for details.

## Changelog

### Version 1.0.0
- Initial release
- Payment method detection and labeling
- Conditional QR code display
- Enhanced typography for thermal printers
- Compatible with Odoo 19 Enterprise
