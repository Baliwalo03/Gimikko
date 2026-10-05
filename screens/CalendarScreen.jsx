import { StyleSheet, Text, View } from 'react-native';
import { Calendar } from 'react-native-calendars';

export default function CalendarScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Your Events</Text>
      <Calendar
        style={styles.calendar}
        onDayPress={(day) => console.log('selected day', day.dateString)}
        theme={{
          backgroundColor: '#ffffff',
          calendarBackground: '#ffffff',
          textSectionTitleColor: '#05dd00',
          selectedDayBackgroundColor: '#05dd00',
          selectedDayTextColor: '#ffffff',
          todayTextColor: '#05dd00',
          dayTextColor: '#2d4150',
          monthTextColor: '#333333',
          textDisabledColor: '#d9e1e8',
          arrowColor: '#05dd00',
          monthTextFontWeight: 'bold',
          textDayFontWeight: '500',
          textMonthFontWeight: 'bold',
          textDayHeaderFontWeight: '600',
        }}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#ffffff',
    paddingTop: 48,
    paddingHorizontal: 16,
  },
  title: {
    fontSize: 24,
    fontWeight: '700',
    color: '#05dd00',
    marginBottom: 12,
  },
  calendar: {
    borderRadius: 16,
    elevation: 2,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.08,
    shadowRadius: 6,
  },
});
