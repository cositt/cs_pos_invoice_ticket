# -*- coding: utf-8 -*-
{
    'name': 'Configuración Ticket Factura',
    'version': '1.0.0',
    'category': 'Sales/Point of Sale',
    'summary': 'Personalización del ticket post-pago TPV Restaurante',
    'description': """
Personalización del ticket de cliente/factura simplificada del TPV Restaurante.

Funcionalidades:
- Muestra método de pago (efectivo / tarjeta / mixto)
- QR de factura solo si el pago es 100% con tarjeta
- Tamaño de letra aumentado para mejor legibilidad
- Cabecera: datos de empresa más legibles; logo dimensionado para térmica
- Compatible con impresoras térmicas de 80mm

Técnico:
- Extiende point_of_sale.OrderReceipt y point_of_sale.ReceiptHeader vía t-inherit
- Usa is_cash_count para detectar efectivo (true) vs tarjeta (false)
- Compatible con Odoo 19 Enterprise
    """,
    'author': 'Cositt Technology',
    'website': 'https://cositt.com',
    'license': 'LGPL-3',
    'depends': [
        'point_of_sale',
        'pos_restaurant',
    ],
    'data': [],
    'assets': {
        'point_of_sale._assets_pos': [
            'cs_pos_invoice_ticket/static/src/scss/receipt.scss',
            'cs_pos_invoice_ticket/static/src/js/order_receipt.js',
            'cs_pos_invoice_ticket/static/src/xml/receipt_header.xml',
            'cs_pos_invoice_ticket/static/src/xml/order_receipt.xml',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
