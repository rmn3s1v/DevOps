import { mount } from "@vue/test-utils"
import SensorList from "../SensorList.vue"
import { describe, it, expect } from "vitest"

describe("SensorList", () => {
  it("renders sensors", () => {
    const wrapper = mount(SensorList, {
      props: {
        sensors: [
          { id: 1, name: "Test", data_type: "temperature" }
        ]
      }
    })

    expect(wrapper.text()).toContain("Test")
  })
})
