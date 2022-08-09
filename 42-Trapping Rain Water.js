/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function (height) {
    let maxLeft = new Array(height.length).fill(0)
    let maxRight = new Array(height.length).fill(0)
    for (let index = 1; index < height.length; index++) {
        maxLeft[index] = Math.max(maxLeft[index - 1], height[index - 1])

    }
    for (let index = height.length - 2; index >= 0; index--) {
        maxRight[index] = Math.max(maxRight[index + 1], height[index + 1])

    }
    let trappedWater = 0;
    for (let index = 0; index < height.length; index++) {
        let waterLevel = Math.min(maxLeft[index], maxRight[index])
        let curTrappedWater = waterLevel - height[index]
        if (curTrappedWater > 0) {
            trappedWater = trappedWater + curTrappedWater
        }

    }
    return trappedWater
};
