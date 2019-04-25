class Bag {
  /**
   * Create a new Form instance.
   *
   * @param {object} data
   */
    constructor(data) {
        //this.originalData = data;
        for (let field in data) {
            this[field] = data[field];
        }
    }

    mergeWith(value) {
        //var data = this.data();
        for(var i in value) {
            this[i] = value[i];
        }

        return this;
    }

    /**
    * Fetch all relevant data for the form.
    */
    data() {
        let data = {};

        for (let property in this.originalData) {
            data[property] = this[property];
        }

        return data;
    }
}


//export default Bag;
