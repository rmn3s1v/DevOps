import { mount, flushPromises } from "@vue/test-utils"
import { describe, it, expect, vi } from "vitest"

vi.mock("../../api/api", () => ({
  getSensors: vi.fn()
}))

import { getSensors } from "../../api/api"
import SensorList from "../SensorList.vue"

describe("SensorList", () => {
  it("renders sensors", async () => {
    getSensors.mockResolvedValue({
      data: [
        { id: 1, name: "Test", data_type: "temperature" }
      ]
    })

    const wrapper = mount(SensorList)

    await flushPromises()

    expect(wrapper.text()).toContain("Test")
  })
})
