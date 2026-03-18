import { mount } from "@vue/test-utils"
import { describe, it, expect, vi } from "vitest"

vi.mock("../api/api", () => ({
  createSensor: vi.fn()
}))

import * as api from "../api/api"
import SensorForm from "../components/SensorForm.vue"

describe("SensorForm", () => {
  it("creates sensor and emits created", async () => {
    api.createSensor.mockResolvedValue({})

    const wrapper = mount(SensorForm)

    const inputs = wrapper.findAll("input")

    await inputs[0].setValue("Sensor1")
    await inputs[1].setValue("1.1.1.1")

    await wrapper.find("select").setValue("temperature")

    await wrapper.find("form").trigger("submit.prevent")

    expect(api.createSensor).toHaveBeenCalledWith({
      name: "Sensor1",
      ip: "1.1.1.1",
      data_type: "temperature"
    })

    expect(wrapper.emitted("created")).toBeTruthy()
  })
})
