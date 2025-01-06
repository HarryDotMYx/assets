export const parseJSONSafely = (jsonString, fallback = []) => {
    try {
        return JSON.parse(jsonString);
    } catch (error) {
        console.error('JSON parsing error:', error);
        return fallback;
    }
};