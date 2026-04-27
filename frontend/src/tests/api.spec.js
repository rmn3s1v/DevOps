import { describe, it, expect, vi, beforeEach } from "vitest";
import axios from "axios";

vi.mock("axios", () => {
  const mockApi = {
    get: vi.fn(),
    post: vi.fn(),
    put: vi.fn(),
    delete: vi.fn(),
  };

  return {
    default: {
      create: vi.fn(() => mockApi),
    },
  };
});

describe("api module", async () => {
  let apiModule;
  let mockApi;

  beforeEach(async () => {
    vi.clearAllMocks();
    vi.resetModules();

    apiModule = await import("../api/api.js");
    mockApi = axios.create.mock.results[0].value;
  });

  it("creates axios instance with /api baseURL", () => {
    expect(axios.create).toHaveBeenCalledWith({ baseURL: "/api" });
  });

  it("calls sensor CRUD endpoints", () => {
    apiModule.getSensors();
    expect(mockApi.get).toHaveBeenCalledWith("/sensors");

    const sensor = { name: "Temperature", type: "temp" };
    apiModule.createSensor(sensor);
    expect(mockApi.post).toHaveBeenCalledWith("/sensors", sensor);

    apiModule.updateSensor("1", sensor);
    expect(mockApi.put).toHaveBeenCalledWith("/sensors/1", sensor);

    apiModule.deleteSensor("1");
    expect(mockApi.delete).toHaveBeenCalledWith("/sensors/1");
  });

  it("calls sensor data CRUD endpoints", () => {
    apiModule.getSensorData("sensor-1");
    expect(mockApi.get).toHaveBeenCalledWith("/sensors/sensor-1/data");

    const payload = { value: 25 };
    apiModule.createSensorData("sensor-1", payload);
    expect(mockApi.post).toHaveBeenCalledWith("/sensors/sensor-1/data", payload);

    apiModule.updateSensorData("sensor-1", "data-1", payload);
    expect(mockApi.put).toHaveBeenCalledWith(
      "/sensors/sensor-1/data/data-1",
      payload
    );

    apiModule.deleteSensorData("sensor-1", "data-1");
    expect(mockApi.delete).toHaveBeenCalledWith(
      "/sensors/sensor-1/data/data-1"
    );
  });
});
