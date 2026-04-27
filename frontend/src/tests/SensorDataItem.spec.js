import { mount } from "@vue/test-utils";
import { describe, it, expect, vi, beforeEach } from "vitest";
import SensorDataItem from "../components/SensorDataItem.vue";
import { updateSensorData, deleteSensorData } from "../api/api";

vi.mock("../api/api", () => ({
  updateSensorData: vi.fn(),
  deleteSensorData: vi.fn(),
}));

describe("SensorDataItem", () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it("renders temperature value and timestamp", () => {
    const wrapper = mount(SensorDataItem, {
      props: {
        sensor: {
          id: 1,
          data_type: "temperature",
        },
        data: {
          id: 10,
          temperature: 25.5,
          timestamp: "2026-04-27 20:00",
        },
      },
    });

    expect(wrapper.text()).toContain("25.5");
    expect(wrapper.text()).toContain("2026-04-27 20:00");
  });

  it("renders humidity value", () => {
    const wrapper = mount(SensorDataItem, {
      props: {
        sensor: {
          id: 1,
          data_type: "humidity",
        },
        data: {
          id: 11,
          humidity: 60,
          timestamp: "2026-04-27 20:01",
        },
      },
    });

    expect(wrapper.text()).toContain("60");
  });

  it("renders pressure value", () => {
    const wrapper = mount(SensorDataItem, {
      props: {
        sensor: {
          id: 1,
          data_type: "pressure",
        },
        data: {
          id: 12,
          pressure: 760,
          timestamp: "2026-04-27 20:02",
        },
      },
    });

    expect(wrapper.text()).toContain("760");
  });

  it("renders light value", () => {
    const wrapper = mount(SensorDataItem, {
      props: {
        sensor: {
          id: 1,
          data_type: "light",
        },
        data: {
          id: 13,
          light: 100,
          timestamp: "2026-04-27 20:03",
        },
      },
    });

    expect(wrapper.text()).toContain("100");
  });

  it("switches to edit mode and cancels editing", async () => {
    const wrapper = mount(SensorDataItem, {
      props: {
        sensor: {
          id: 1,
          data_type: "temperature",
        },
        data: {
          id: 10,
          temperature: 25.5,
          timestamp: "2026-04-27 20:00",
        },
      },
    });

    await wrapper.findAll("button")[0].trigger("click");

    expect(wrapper.find("input").exists()).toBe(true);
    expect(wrapper.find("input").element.value).toBe("25.5");

    await wrapper.findAll("button")[1].trigger("click");

    expect(wrapper.find("input").exists()).toBe(false);
  });

  it("updates sensor data and emits reload", async () => {
    updateSensorData.mockResolvedValue({});

    const wrapper = mount(SensorDataItem, {
      props: {
        sensor: {
          id: 1,
          data_type: "temperature",
        },
        data: {
          id: 10,
          temperature: 25.5,
          timestamp: "2026-04-27 20:00",
        },
      },
    });

    await wrapper.findAll("button")[0].trigger("click");

    const input = wrapper.find("input");
    await input.setValue("30");

    await wrapper.findAll("button")[0].trigger("click");

    expect(updateSensorData).toHaveBeenCalledWith(1, 10, {
      temperature: 30,
    });
    expect(wrapper.emitted("reload")).toBeTruthy();
  });

  it("deletes sensor data and emits reload", async () => {
    deleteSensorData.mockResolvedValue({});

    const wrapper = mount(SensorDataItem, {
      props: {
        sensor: {
          id: 1,
          data_type: "temperature",
        },
        data: {
          id: 10,
          temperature: 25.5,
          timestamp: "2026-04-27 20:00",
        },
      },
    });

    await wrapper.findAll("button")[1].trigger("click");

    expect(deleteSensorData).toHaveBeenCalledWith(1, 10);
    expect(wrapper.emitted("reload")).toBeTruthy();
  });
});
