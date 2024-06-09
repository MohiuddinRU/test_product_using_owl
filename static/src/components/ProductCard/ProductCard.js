/** @odoo-module **/

import {Component, xml, mount, whenReady, useState, onWillStart, onMounted} from "@odoo/owl"

export class ProductCard extends Component {
    static template = "test_product_using_owl.ProductCard"
    static props = {
        id: Number,
        name: String,
        list_price: Number
    };
    setup() {
        console.log("inside the ProductCard", this)
        onMounted(() => {
            console.log("props", this.props)
        })
    }
}
