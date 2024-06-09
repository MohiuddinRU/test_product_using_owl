/** @odoo-module **/


import { Component, xml, mount, whenReady, useState, onWillStart, onMounted } from "@odoo/owl"
import { templates } from "@web/core/assets"
import { ProductCard } from "@test_product_using_owl/components/ProductCard/ProductCard"
import { useService } from "@web/core/utils/hooks";

import { jsonrpc } from "@web/core/network/rpc_service";

export class ProductSearchPage extends Component {
    static template = "test_product_using_owl.ProductSearchPage";
    static components = { ProductCard }
    setup() {
        this.state = useState({
            products: []
        });
        onMounted(async () => {
            const res = await jsonrpc("/shop/products")
            this.state.products = res
            console.log("res", this.state)
        })
    }
}

whenReady(() => {
    const element = document.querySelectorAll('.owl_template_here');
    if (element.length > 0) {
        element.forEach(el => mount(ProductSearchPage, el, { templates }))
    }
})

