import { mount } from "@vue/test-utils"
import { describe, it, expect, vi } from "vitest"

vi.mock("../api/api", () => ({
  deleteSensor: vi.fn(),
  updateSensor: vi.fn()
}))

import * as api from "../api/api"
import SensorItem from "../components/SensorItem.vue"

describe("SensorItem", () => {
  it("deletes sensor and emits reload", async () => {
    api.deleteSensor.mockResolvedValue({})

    const wrapper = mount(SensorItem, {
      props: {
        sensor: {
          id: 1,
          name: "Test",
          ip: "1.1.1.1",
          data_type: "temperature"
        }
      }
    })

    const buttons = wrapper.findAll("button")
    await buttons[1].trigger("click")

    expect(api.deleteSensor).toHaveBeenCalledWith(1)
    expect(wrapper.emitted("reload")).toBeTruthy()
  })
  it("updates sensor on save", async () => {
  api.updateSensor.mockResolvedValue({})

  const wrapper = mount(SensorItem, {
    props: {
      sensor: {
        id: 1,
        name: "Old",
        ip: "1.1.1.1",
        data_type: "temperature"
      }
    }
  })

  // нажимаем Edit
  const buttons = wrapper.findAll("button")
  await buttons[0].trigger("click")

  const inputs = wrapper.findAll("input")

  await inputs[0].setValue("NewName")
  await inputs[1].setValue("2.2.2.2")

  await wrapper.find("select").setValue("humidity")

  // Save
  const saveBtn = wrapper.findAll("button")[0]
  await saveBtn.trigger("click")

  expect(api.updateSensor).toHaveBeenCalledWith(1, {
    name: "NewName",
    ip: "2.2.2.2",
    data_type: "humidity"
  })

  expect(wrapper.emitted("reload")).toBeTruthy()
})
})
