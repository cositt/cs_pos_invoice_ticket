/** @odoo-module **/

import { OrderReceipt } from "@point_of_sale/app/screens/receipt_screen/receipt/order_receipt";
import { patch } from "@web/core/utils/patch";

patch(OrderReceipt.prototype, {
    /**
     * Devuelve true si TODOS los pagos son con tarjeta (no efectivo).
     * is_cash_count = true  → efectivo
     * is_cash_count = false → tarjeta / banco
     */
    isCardOnlyPayment() {
        const lines = this.paymentLines;
        if (!lines || lines.length === 0) return false;
        return lines.every((line) => line.payment_method_id && !line.payment_method_id.is_cash_count);
    },
});
